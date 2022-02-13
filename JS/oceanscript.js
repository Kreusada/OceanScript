'use strict';

const ROW_INDICATORS = "^~_"
const COLUMN_INDICATORS = "<->"
const R1S = "abcjklstu123"
const R2S = "defmnovwx456"
const R3S = "ghipqryz0789"
const R1S1S = "ajs1"
const R1S2S = "bkt2"
const R1S3S = "clu3"
const R2S1S = "dmv4"
const R2S2S = "enw5"
const R2S3S = "fox6"
const R3S1S = "gpy7"
const R3S2S = "hqz8"
const R3S3S = "ir09"

const MUL_MAPPING = {
    0: 1,
    1: 1,
    2: 1,
    3: 2,
    4: 2,
    5: 2,
    6: 3,
    7: 3,
    8: 3,
    9: 4,
    10: 4,
    11: 4,
}

function OceanScriptError(char, position) {
    const error = new Error(`${char} (position ${position})`);
    error.code = "OCEANSCRIPT_ERROR";
    error.position = position;
    return error;
}

OceanScriptError.prototype = Object.create(Error.prototype);

function encode(text) {
    text = text.trim();
    var ret = "";
    for (var i = 0; i < text.length; i++) {
        var char = text[i];
        if (char == char.toUpperCase()) {
            ret += "*";
        }
        var char = char.toLowerCase();
        if (R1S.includes(char)) {
            ret += "^";
            if (R1S1S.includes(char)) {
                ret += "<";
            }
            else if (R1S2S.includes(char)) {
                ret += "-";
            }
            else {
                ret += ">";
            }
            ret += ".".repeat(MUL_MAPPING[R1S.indexOf(char)]);
        }
        else if (R2S.includes(char)) {
            ret += "~";
            if (R2S1S.includes(char)) {
                ret += "<";
            }
            else if (R2S2S.includes(char)) {
                ret += "-";
            }
            else {
                ret += ">";
            }
            ret += ".".repeat(MUL_MAPPING[R2S.indexOf(char)]);
        }
        else if (R3S.includes(char)) {
            ret += "_";
            if (R3S1S.includes(char)) {
                ret += "<";
            }
            else if (R3S2S.includes(char)) {
                ret += "-";
            }
            else {
                ret += ">";
            }
            ret += ".".repeat(MUL_MAPPING[R3S.indexOf(char)]);
        }
        else if (char == " ") {
            ret += ",";
        }
        else if (char == "\n") {
            ret += "%";
        }
        else {
            ret += "=" + char;
        }
    }
    return ret;
}

// function decode(text) {
//     var regex = /(\*?=.)|(\\n|,|%)|(\*?[\^~_][>\-<]\.{1,4})/;
//     var chunks = text.split(regex).filter(x => !!x);
//     var message = "";
//     for (const [i, j] of chunks.entries()) {
//         if (",\n".includes(j)) {
//             message += " ";
//             continue;
//         }
//         if (j == "%") {
//             message += "\n";
//             continue;
//         }
//         if (j.length < 2) {
//             throw new OceanScriptError(`invalid syntax '${j}'`)
//         }
//         if (j[0] == "*") {
//         }
//     }
// }

module.exports = {
    encode: encode,
    OceanScriptError: OceanScriptError
};
