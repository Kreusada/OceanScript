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
    0: '.',
    1: '.',
    2: '.',
    3: '..',
    4: '..',
    5: '..',
    6: '...',
    7: '...',
    8: '...',
    9: 'o',
    10: 'o',
    11: 'o',
}

const UPPER = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

function encode(text) {
    var ret = "";
    for (var i = 0; i < text.length; i++) {
        var char = text[i];
        if (UPPER.includes(char)) {
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
            ret += MUL_MAPPING[R1S.indexOf(char)];
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
            ret += MUL_MAPPING[R2S.indexOf(char)];
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
            ret += MUL_MAPPING[R3S.indexOf(char)];
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
