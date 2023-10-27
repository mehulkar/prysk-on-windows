// disable package manager update notifiers
import { execSync } from "child_process";
import { getVenvBin, isWindows } from "./util.mjs";

process.env.NO_UPDATE_NOTIFIER = 1;
const specificTest = process.argv[2];

const pryskBin = getVenvBin("prysk");

console.log(`Running ${specificTest || "all"} tests... with ${pryskBin}`);

const testArg = specificTest ? `tests/${specificTest}` : "tests";

console.log("running which bash:");
const bashBuffer = execSync(`which bash`); // no stdio: inherit so we can capture output

let bash = bashBuffer.toString().trim();

bash = isWindows ? bash + ".exe" : bash;

console.log("location of bash:", bash);

try {
  execSync(`${pryskBin} "${testArg}"`, {
    stdio: "inherit",
  });
} catch (e) {
  console.log("something went wrong", e);
  // Swallow the node error stack trace. stdio: inherit should
  // already have the test failures printed. We don't need the Node.js
  // execution to also print its stack trace from execSync.
  process.exit(1);
}
