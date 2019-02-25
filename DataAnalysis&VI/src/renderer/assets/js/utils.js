// 用来判断数组中否含有某个元素，返回索引和布尔值
export function contains(needle, array) {
    let len = array.length,
        obj = {
            index: -1,
            bool: false
        };
    for (let i = 0; i < len; i++) {
        if (needle === array[i]) {
            obj.index = i,
            obj.bool = true;
            return obj
        } else {
            return obj;
        }
    }
}

// 截取某个字符串中某个字符的前或者后的字符,如果传入字符是1，就返回前面的字符，传入字符是其他就返回后面的
export function getStr(string, str,) {
    let index = string.lastIndexOf(str); //查找最后一个str出现的位置
    let ss = string.slice(index, string.length); // 截取从当前位置到最后一个字符的所有字符返回
    return ss;
}

export function randomString(len, charSet) {
    charSet = charSet || 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
    let randomString = '';
    for (var i = 0; i < len; i++) {
        let randomPoz = Math.floor(Math.random() * charSet.length);
        randomString += charSet.substring(randomPoz, randomPoz + 1);
    }
    return randomString;
}

export function getNowFormatDate() {
    var date = new Date();
    var seperator1 = "-";
    var seperator2 = ":";
    var month = date.getMonth() + 1;
    var strDate = date.getDate();
    if (month >= 1 && month <= 9) {
        month = "0" + month;
    }
    if (strDate >= 0 && strDate <= 9) {
        strDate = "0" + strDate;
    }
    var currentdate = date.getFullYear() + seperator1 + month + seperator1 + strDate
            + " " + date.getHours() + seperator2 + date.getMinutes()
            + seperator2 + date.getSeconds();
    return currentdate;
}

export function changeStr2Float(s) {
    var str = s.replace(" ", "")
    if (str === undefined || str === null || str === "") {
        return null
    } else {
        var fresult = parseFloat(str);
        if (isNaN(fresult)) {
            return null
        } else {
            return fresult
        }
    }
}