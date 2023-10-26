import { execSync } from "child_process";
import { debugVenv, getVenvBin, makeVenv } from "./util.mjs";

makeVenv();

debugVenv();

const python3 = getVenvBin("python3");
const pip = getVenvBin("pip");

console.log("install latest pip");
execSync(`${python3} -m pip install --quiet --upgrade pip`, {
  stdio: "inherit",
});

console.log("instapp prysk@15");
execSync(`${pip} install "prysk==0.15.0"`, { stdio: "inherit" });
