// Respect an active virtual environment or an explicit interpreter path.
import { spawnSync } from 'node:child_process';
const result = spawnSync(process.env.PYTHON || 'python', process.argv.slice(2), { stdio: 'inherit' });
if (result.error) console.error(result.error.message);
process.exit(result.status ?? 1);
