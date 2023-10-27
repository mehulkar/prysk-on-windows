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

execSync(`${pryskBin} --shell="bash" "${testArg}"`, {
  stdio: "inherit",
});
