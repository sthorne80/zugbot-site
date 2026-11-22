interface Entry { location: string; title: string; text: string }
interface DocumentEntry { path: string; label: string; title: string; excerpt: string; haystack: string }
const results = document.querySelector<HTMLElement>('[data-results]')!;
const status = document.querySelector<HTMLElement>('[data-search-status]')!;
const list = document.querySelector<HTMLUListElement>('[data-result-list]')!;
const input = document.querySelector<HTMLInputElement>('#manual-query')!;
let index: Promise<DocumentEntry[]> | undefined;

async function loadIndex(): Promise<DocumentEntry[]> {
  const response = await fetch('/search/search_index.json');
  if (!response.ok) throw new Error('Index unavailable');
  const {docs}: {docs: Entry[]} = await response.json();
  const titles = new Map(docs.filter(entry => !entry.location.includes('#')).map(entry => [entry.location, entry.title]));
  const template = document.createElement('template');
  return docs.map(entry => {
    template.innerHTML = entry.text;
    const excerpt = (template.content.textContent ?? '').replace(/\s+/g, ' ').trim();
    const label = titles.get(entry.location.split('#')[0]) || entry.title;
    return {path: '/' + entry.location, title: entry.title, label, excerpt, haystack: (entry.title+' '+label+' '+excerpt).toLowerCase()};
  });
}

function snippet(text: string, terms: string[]) {
  const found = terms.map(term => text.toLowerCase().indexOf(term)).filter(i => i >= 0);
  const start = found.length ? Math.max(0, Math.min(...found) - 38) : 0;
  return (start ? '…' : '') + text.slice(start, start + 160) + (start + 160 < text.length ? '…' : '');
}

async function search(scroll: boolean) {
  const query = input.value.trim();
  results.hidden = !query;
  list.replaceChildren();
  if (!query) { status.textContent = ''; return; }
  status.textContent = 'Searching…';
  if (scroll) results.scrollIntoView({block:'start'});
  let entries: DocumentEntry[];
  try { index ??= loadIndex(); entries = await index; }
  catch {
    index = undefined;
    if (input.value.trim() === query) status.textContent = 'Search could not load. Try again or browse the guides below.';
    return;
  }
  if (input.value.trim() !== query) return;
  const phrase = query.toLowerCase();
  const terms = phrase.split(/\s+/).filter(Boolean);
  const hits = entries.filter(entry => terms.every(term => entry.haystack.includes(term))).map(entry => {
    const title = entry.title.toLowerCase();
    const score = (title === phrase ? 100 : 0) + (title.includes(phrase) ? 15 : 0)
      + terms.reduce((total, term) => total + (title.includes(term) ? 4 : 0), 0) + (entry.path.includes('#') ? 1 : 0);
    return {entry, score};
  }).sort((a,b) => b.score - a.score);
  status.textContent = hits.length ? hits.length + (hits.length === 1 ? ' match' : ' matches') + ' for “' + query + '”.' : 'No matches for “' + query + '”. Try a command, a game mode, or a shorter phrase.';
  for (const {entry} of hits) {
    const li = document.createElement('li'), link = document.createElement('a');
    const title = document.createElement('strong'), detail = document.createElement('span');
    link.href = entry.path;
    title.textContent = entry.title === entry.label ? entry.title : entry.label + ' · ' + entry.title;
    detail.textContent = snippet(entry.excerpt, terms);
    link.append(title, detail); li.append(link); list.append(li);
  }
}

function updateUrl() {
  const url = new URL(location.href);
  const q = input.value.trim();
  if (q) url.searchParams.set('q', q); else url.searchParams.delete('q');
  history.replaceState(null, '', url);
}
let timer: ReturnType<typeof setTimeout>;
input.addEventListener('input', () => {
  clearTimeout(timer);
  timer = setTimeout(() => { updateUrl(); void search(false); }, 150);
});
input.form!.addEventListener('submit', event => {
  event.preventDefault(); clearTimeout(timer); updateUrl(); void search(true);
});
input.value = new URL(location.href).searchParams.get('q')?.slice(0,180) || '';
if (input.value) void search(true);
