var data = {
    "0": 3709383275,
    "1": 1650252000, // serverTimeNow
    "2": 1650252706, // timeNow
    "3": 1810264575,
    "4": 7,
    "5": 10,
    "6": 5,
    "7": 0, // mouseMove
    "8": 0, // mouseclick
    "9": 0, // mouseWhell
    "10": 0,  // keyDown
    "11": 0,  // clickPos.x
    "12": 0,  // clickPos.y
    "13": 3748,
    "14": 0,
    "15": 0, // 0
    "16": 2,  // 次数
    "17": 3,
    "base_fileds": [
        4,
        4,
        4,
        4,
        1,
        1,
        1,
        3,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        4,
        2,
        1
    ]
};

data = {
    "0": 3709383275,
    "1": 1650261000,
    "2": 1650261972,
    "3": 1810264575,
    "4": 7,
    "5": 10,
    "6": 5,
    "7": 0,
    "8": 0,
    "9": 0,
    "10": 0,
    "11": 0,
    "12": 0,
    "13": 3748,
    "14": 0,
    "15": 0,
    "16": 1,
    "17": 3,
    "base_fileds": [
        4,
        4,
        4,
        4,
        1,
        1,
        1,
        3,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        4,
        2,
        1
    ]
}

var m ='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-_';
function toBuffer(data) {
    for (var a = 'base_f', u = data[a + 'ileds'], c = [], s = -1, v = 0, f = u['length']; v < f; v++)
        for (var l = data[v], p = u[v], d = s += p; c[d] = l & parseInt('255', 10),
            --p != 0;)
            --d,
                l >>= parseInt(10, 8);
    return c
};

function g(n, a, o, i, u) {
    for (var c = '11', v = '11', f = n['length']; a < f;)
        o[i++] = n[a++] ^ u & parseInt(c + v + '11' + '11', 2),
            u = ~(u * parseInt('203', 8))
}

function w(n) {
    for (var t = '0', i = 0, v = n['length'], f = []; i < v;) {
        var l = n[i++] << parseInt('1'+ t, 16) | n[i++] <<8 | n[i++];
        f.push(m.charAt(l >> parseInt('22', 8)), m.charAt(l >> parseInt('12', 10) & parseInt('111111', 2)), m.charAt(l >> 6 & parseInt('6'+ '3', 10)), m.charAt(l & parseInt('3f', 16)))
    }
    return f.join('')
}

function x(n) {
    // var t = o;
    // t = Vn;
    for (var e = 0, i = 0, u = n['length']; i < u; i++)
        e = (e << 5) - e + n[i];
    return e & parseInt('11111111', 2)
}

function N(n) {
    // var t = et;
    var r = x(n)
        , e = [3, r];
    return g(n, +0, e, +2, r),
        // t = P,
        w(e)
};

var n = toBuffer(data);
console.log(N(n))
