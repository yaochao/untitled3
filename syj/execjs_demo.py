#!/usr/bin/env python3
# -*- coding:utf-8 -*- 
# Created by yaochao at 2018/2/28

import execjs

js_f = '''
// 本文件为所有的函数定义，为临时文件
function _$gK(_$nd, _$i2) {; if (_$nd["startsWith"]) return _$nd["startsWith"](_$i2); return _$nd["substr"](0, _$i2["length"]) === _$i2; }

function _$a7() {
    var _$nd = window["navigator"],
        _$i2;
    var _$pY = _$nd["userAgent"];
    if (_$nd["standalone"] !== _$u4) {
        _$ps |= 1073741824;
        _$ps |= 1048576;
        _$ps |= 67108864;
        if (_$ro(window, "$PreUCBrowserClassic,UCBrowserMessageCenter")) _$cW(15);
        else if (_$pY["indexOf"]("MicroMessenger") != -1) _$cW(22);
        else if (_$ro(window, "__firefox__,_firefox_ReaderMode")) _$cW(2);
        else if (_$ro(window, "__mttCreateFrame,mttCumstomJS")) _$cW(16);
        else if (_$ro(window, "__crWeb,__gCrWeb")) _$cW(1);
        else if (_$ro(window, "SeMobFillFormTool,SogouMse") || _$pY["lastIndexOf"]("Sogou") != -1) _$cW(21);
        else if ((/[iPhone|iPod|iPad]\sOS\s10/ ["test"](_$pY) && window["ApplePaySession"] == _$u4) || _$pY["indexOf"]("Safari") == -1) _$cW(23);
        else _$cW(3);
        return;
    }
    var _$ei = _$vB();
    if (_$ei >= 6) {
        _$oG(524288, _$ei);
        if (_$ei >= 10)
            if (!window["indexedDB"] && (window["PointerEvent"] || window["MSPointerEvent"])) _$i2 = 1;
    }
    if (_$ro(window, "msCredentials")) { _$oG(8388608, 4); if (!window["indexedDB"]) _$i2 = 1; }
    if (_$nd["webkitPersistentStorage"]) {
        _$s8(16777216);
        if (_$ro(window, "browser_parameters,item") || !_$ro(window, "openDatabase")) _$cW(20);
        else if (_$ro(window, "FaveIconJavaInterface,jesion")) _$cW(17);
        else if (_$pY["indexOf"](" OPR/") !== -1) _$cW(19);
        else _$cW(1);
        if (window["chrome"] && !window["chrome"]["runtime"])
            if (!window["chrome"]["webstore"]) {} else if (window["onautocomplete"] !== _$u4 && window["document"]["onautocomplete"] !== _$u4 && !window["PerformanceObserver"] && !window["PerformanceObserverEntryList"]) _$cW(24);
        else if (window["Entity"] && !window["AnalyserNode"]) {} else if (window["external"]["AddSearchProvider"] && !window["dumpAll"]) {} else if (window["external"]["GetNextReqID"] && window["external"]["GetOriginalUrl"]) {} else window._$y1 = 1;
    }
    if ("MozAppearance" in document["documentElement"]["style"]) _$oG(33554432, 2);
    if (_$ro(window, "UCWebExt,ucweb")) _$cW(15);
    else if (_$ro(window, "qb_bridge,qbbookshelf")) _$cW(16);
    else if (_$ro(window, "dolphin,dolphininfo,dolphinmeta")) _$cW(18);
    else if (_$pY["indexOf"]("MicroMessenger") != -1) _$cW(22);
    var _$l1 = window["safari"];
    if (_$l1 && _$l1["pushNotification"]) _$oG(67108864, 3);
    if (window["orientation"] !== _$u4) _$ps |= 1073741824;
    if (_$u9()) _$ps |= 2147483648;
    if (_$ro(window, "callPhantom,_phantom")) _$oG(134217728, 30);
    else if (_$ro(window, "$hook$,$$logger,$$lsp,$$lsrb")) _$oG(134217728, 33);
    else if (_$ro(window, "netsparker,__ns")) _$oG(134217728, 36);
    else if (_$ro(window, "hp_identifier")) _$oG(134217728, 34);
    else if (_$eK()) _$oG(134217728, 32);
    else if (_$ro(window, "spi_hooked,mozAnimationStartTime,mozIndexedDB,mozRequestAnimationFrame"))
        if (window["Gamepad"]) {} else _$oG(134217728, 35);
    else if (window._$y1) _$oG(134217728, 31);
    else if (window["Entity"] && !window["FileReader"]) _$oG(134217728, 37);
    else if (window["QTP_EPE_HOOK"] || window._$zp) _$oG(134217728, 38);
    _$jo(function(_$ta) { if (_$ta) _$ps |= 262144; });
}

function _$vQ(_$nd) {
    if (_$oN > 0) {
        _$tT += (_$ws() - _$oN);
        _$fn = _$tT / _$yo;
        _$oN = 0;
        _$dW(4);
    }
}

function _$r1(_$nd) { if (!localStorage) return; for (var _$i2 = 5; _$i2 < 13; _$i2++) { var _$pY = _$tz(_$i2); if (_$pY) _$nd[_$i2] = _$pY; } }

function _$a9(_$nd) {;
    _$wC("$_fh0", _$nd ? _$zQ(_$jv(_$nd)) : "");
}

function _$dq(_$nd) {
    if (_$nd["charAt"](0) !== "/") {
        _$nd = _$s9(_$nd, '?');
        var _$i2 = _$vu;
        if (!(_$jd & 1)) _$i2 = _$cr();
        if (_$zG && !(_$gK(_$i2, '/'))) _$i2 = '/' + _$i2;
        if (_$nd[0] == '') _$nd = _$i2 + _$nd[1];
        else _$nd = _$tt(_$i2) + _$nd[0] + _$nd[1];
    }
    return _$aL(_$nd);
}

function _$hm() {
    _$xF = _$uM(9);
    _$w7 = _$uM(1);
    _$uR = false;
    _$vu = _$uM(2) || _$w7;
    _$s3 = _$u6('', _$uM(3));
    _$bS = _$aK(_$vi(18));
    _$vD = _$aK(_$vi(17));
    _$jd = _$aK(_$vi(16));
    _$tQ = {}, _$qs = {};
    var _$nd = _$uM(10);
    if (_$nd) { var _$i2 = _$nd["split"](';'); for (var _$pY = 0; _$pY < _$i2["length"]; _$pY++) { var _$ei = _$it(_$i2[_$pY], "="); if (_$ei[0] && _$ei[1]) _$tQ[_$ei[0]] = _$ei[1]; } }
    var _$l1 = _$uM(11);
    if (_$l1) { var _$ta = _$l1["split"](';'); for (var _$pY = 0; _$pY < _$ta["length"]; _$pY++) { var _$qm = _$it(_$ta[_$pY], "="); if (_$qm[0] && _$qm[1]) _$qs[_$qm[0]] = _$qm[1]; } }
    _$vC = Number(_$uM(25));
    _$vN = _$ws();
}

function _$vT(_$nd, _$i2) {
    var _$pY = ["setRequestHeader", "abort", "addEventListener", "dispatchEvent", "removeEventListener", "getAllResponseHeaders", "getResponseHeader", "overrideMimeType"],
        _$ei = {},
        _$l1;

    function _$qm(_$ff) { _$ff = _$j4(_$ff, _$ei["url"], _$i2); return _$nd["send"](_$ff); };

    function _$eB(_$ff, _$xs) {
        _$ei["readyState"] = _$nd["readyState"];
        if (_$nd["readyState"] === 4) {
            _$ei["response"] = _$nd["response"];
            _$ei["responseBody"] = _$nd["responseBody"];
            _$ei["responseText"] = _$nd["responseText"];
            _$ei["responseXML"] = _$nd["responseXML"];
            _$ei["status"] = _$nd["status"];
            _$ei["statusText"] = _$nd["statusText"];
        }
        if (_$ei["onreadystatechange"]) _$ei["onreadystatechange"](_$ff, _$xs);
    }
    for (_$l1 = 0; _$l1 < _$pY["length"]; _$l1++) _$ei[_$pY[_$l1]] = _$lg(_$pY[_$l1]);

    function _$lg(_$ff) {
        return function() {
            switch (arguments["length"]) {
                case 0:
                    return _$nd[_$ff]();
                case 1:
                    return _$nd[_$ff](arguments[0]);
                case 2:
                    return _$nd[_$ff](arguments[0], arguments[1]);
                case 3:
                    return _$nd[_$ff](arguments[0], arguments[1], arguments[2]);
                default:
                    ;
            }
        };
    }
    _$ei["open"] = _$ta;

    function _$ta(_$ff, _$xs, _$vI, _$kc, _$bW) {
        if (_$i2) _$xs = _$tA(_$xs);
        else _$xs = _$v8(_$xs);
        _$ei["url"] = _$xs;
        if (_$kc && _$bW) return _$nd["open"](_$ff, _$xs, _$vI, _$kc, _$bW);
        else return _$nd["open"](_$ff, _$xs, _$vI);
    }
    _$ei["send"] = _$qm;
    _$ei["readyState"] = 0;
    _$ei["onreadystatechange"] = null;
    _$nd["onreadystatechange"] = _$eB;
    return _$ei;
}

function _$wY(_$nd) {
    var _$i2 = _$u4;
    var _$pY = '';
    var _$ei = _$qP(_$fN(_$zy));
    if (_$ei && _$ei["length"] >= _$zd) {
        _$i2 = _$ei["charAt"](0);
        var _$l1 = _$zT(_$ei["substring"](1));
        var _$ta = _$l1[_$zY + 1];
        for (var _$qm = 0; _$qm < _$zY + 1; _$qm++) _$l1[_$qm] ^= _$ta;
        _$pY = _$l1["slice"](0, _$zY + 1);
    }
    var _$eB = _$tG(_$hn());
    if (!_$i2 || _$pY["length"] != _$zY + 1 || _$eB[31] != _$pY[_$zY]) {;
        window["location"]["reload"]();
        return '';
    }
    var _$lg = _$d1();
    if (_$lg <= _$r2) { _$lg = _$r2 + 1; }
    _$r2 = _$lg;
    var _$ff = [];
    _$bb([(_$lg / 0x100000000) & 0xffffffff, _$lg & 0xffffffff], _$ff);
    var _$xs = _$sh(_$nd);
    var _$vI = _$ff["concat"](_$xs);
    var _$kc = _$uc(_$pY["concat"](_$vI));
    for (var _$qm = 0; _$qm < _$zY + 1; _$qm++) _$pY[_$qm] ^= _$kc;
    var _$bW = _$oY(_$eB);
    var _$sK = _$oY(_$tG(_$ly()));
    var _$dE = [];
    for (var _$qm = 0; _$qm < 16; _$qm++) {
        _$dE[_$qm * 2] = _$bW[_$qm];
        _$dE[_$qm * 2 + 1] = _$sK[_$qm];
    }
    var _$f3 = _$eJ(_$vI, _$dE);
    return _$i2 + _$zQ(_$pY["concat"](_$kc, _$f3));
};

function _$vi(_$nd) {
    var _$i2 = _$nd % 64;
    var _$pY = _$nd - _$i2;
    _$i2 = _$tF(_$i2);
    _$i2 ^= _$v4;
    _$pY += _$i2;
    return _$vf[_$pY];
};

function _$co(_$nd, _$i2, _$pY) {; return _$pS((_$pY - _$nd) * 65535 / (_$i2 - _$nd)); };

function _$vs(_$nd, _$i2) {
    var _$pY = localStorage || _$zZ;
    _$pY[_$nd] = _$i2;
};

function _$sl(_$nd) {
    if (_$yn["length"] < 1100) _$yn.push(_$nd["button"], _$nd.x, _$nd.y);
    _$sM++;
    _$op = _$ws();
    _$dW(3);
}

function _$t7() {
    if (_$lT) /$/.test(_$vv());
    var _$nd = new Array(32);
    for (var _$i2 = 0; _$i2 < 32; _$i2++) _$nd[_$i2] = _$i2;
    _$nd = _$rY(_$nd).split('');
    var _$pY = new Array(129);
    for (var _$i2 = 127; _$i2 < 256; _$i2++) _$pY[_$i2 - 127] = _$i2;
    _$pY = _$rY(_$pY).split('');
    _$y2 = 'I-M3DJ0rcufq%d\\1]B:b&yTo2<>HFn};X |9v`[(V#A~Z*5.Cm^OWR{SN/E6pU)K$ztL@8e,jax\'7!lQg4s+w"k?P=i_GYh'.split('');
    _$y2 = _$nd.concat(_$y2.concat(_$pY));
    _$ya = 'AmuI`,4kG^Msg!OY&/8#qN[leC2?9y:wdJ1P$Z<|; %_c"XSxoUW6]HT@}LF.0R{Ei3(-f*p~zhvnQ=7\\+\'rb)Dtj5aVB>K'.split('');
}

function _$qq() {
    var _$nd = new _$wQ();

    function _$i2(_$pY) { try { var _$ei = _$iW(_$pY, _$ly()); return _$ei; } catch (_$l1) {; } }
    _$nd["get"]("$_YWTU", function(_$pY) {
        var _$ei;
        if (_$pY) _$ei = _$i2(_$pY);
        var _$l1;
        var _$ta = _$vi(26);
        if (_$ta) _$l1 = _$i2(_$ta);
        if (_$l1 && _$ei) {
            _$xt = _$ei;
            _$nd["get"]("$_cDro", function(_$qm) {
                _$wE = parseInt(_$qm);
                _$wE = window["isNaN"](_$wE) ? 0 : _$wE;
                _$wE++;
                _$nd["set"]("$_cDro", _$wE);
            });
        } else if (_$l1) {
            _$xt = _$l1;
            _$wE = 0;
            _$nd["set"]("$_YWTU", _$ta);
            _$nd["set"]("$_cDro", _$wE);
        } else if (_$ei) {;
            _$xt = _$ei;
            _$nd["get"]("$_cDro", function(_$qm) { _$wE = _$qm; });
        } else;
    });
}

function _$gP() {
    _$a7();
    _$q5();
    if (!_$wC("$_fh0")) {
        _$wb();
        _$dr();
    }
    _$dW(2);
}

function _$s8(_$nd, _$i2) { if (_$i2 === _$u4 || _$i2) _$ps |= _$nd; };

// trim的实现
function _$ug() { return this["replace"](/^\s+|\s+$/g, ''); };

function _$tL(_$nd) {
    var _$i2;
    try {
        var _$pY = document["createElement"]("a");
        _$pY["href"] = location["href"];
        var _$ei = document["createElement"]("a");
        _$ei["href"] = _$nd;
        _$ei["href"] = _$ei["href"];
        _$i2 = _$pY["protocol"] + "//" + _$pY["host"] !== _$ei["protocol"] + "//" + _$ei["host"];
    } catch (_$l1) { _$i2 = true; }
    return _$i2;
};

function _$sh(_$nd) {
    var _$i2, _$pY;
    _$pf();
    _$cI();
    _$aZ(4, _$wB);
    _$nd = _$nd || 255;
    var _$ei = 0;
    var _$l1 = [1, _$nd];
    _$bb([_$ei, _$ps, _$xg], _$l1);
    _$l1.push(_$hT, _$bZ);
    _$d9(_$l1, _$wt());
    _$pY = _$wC("$_f0", _$vb);
    if (_$pY) {
        _$d9(_$l1, _$zT(_$pY));
        _$ei |= 1;
    }
    if (_$yn["length"] > 0 || _$yu > 0 || _$yl > 0 || _$wn > 0) {
        _$d9(_$l1, _$pS(_$xW));
        _$d9(_$l1, _$pS(_$bH));
        _$d9(_$l1, _$pS(_$sM));
        _$d9(_$l1, _$pS(_$ye));
        _$d9(_$l1, _$pS(_$yo));
        _$d9(_$l1, _$pS(_$yu));
        _$d9(_$l1, _$pS(_$yl));
        _$d9(_$l1, _$pS(_$wn));
        _$d9(_$l1, _$pS(_$yx));
        _$d9(_$l1, _$pS(_$uX));
        _$d9(_$l1, _$pS(_$fn));
        _$ei |= 2;
    }
    _$pY = _$wC("$_fh0");
    if (_$pY) {
        _$d9(_$l1, _$zT(_$pY));
        _$ei |= 4;
    }
    _$pY = _$wC("$_f1", _$sp);
    if (_$pY) {
        _$d9(_$l1, _$zT(_$pY));
        _$ei |= 8;
    }
    if (_$xD != _$u4 || _$t1 != _$u4) {
        _$d9(_$l1, _$pS(_$xD));
        _$d9(_$l1, _$pS(_$t1));
        _$ei |= 16;
    }
    if (_$a8 != _$u4) {
        _$l1.push(_$a8);
        _$d9(_$l1, _$pS(window["Math"]["round"](_$vE)));
        if (_$bN) _$xg |= 2;
        _$ei |= 32;
    }
    var _$ta = _$vz();
    if (_$ta != _$u4) {
        _$l1.push(_$ta);
        _$ei |= 64;
    }
    if (_$aA != _$u4) {
        var _$qm = window["Math"]["round"]((_$ws() - _$aA) / 100.0);
        _$d9(_$l1, _$pS(_$qm));
        _$ei |= 128;
    }
    var _$eB = _$wC("$_fr");
    if (_$eB) {
        _$d9(_$l1, _$zT(_$eB));
        _$ei |= 256;
    }
    if (_$xt && _$wE !== _$u4) {
        _$d9(_$l1, _$xt);
        _$l1.push(_$q0(_$wE));
        _$ei |= 512;
    }
    var _$lg = _$wC("$_fpn1");
    if (_$lg) try {
        _$d9(_$l1, _$zT(_$lg));
        _$ei |= 1024;
    } catch (_$ff) {}
    var _$xs = _$xx();
    if (_$xs != _$u4) {
        _$l1.push(_$xs);
        _$ei |= 2048;
    }
    try {
        _$pY = _$zT(_$wC("$_vvCI"));
        if (_$pY && _$pY["length"] === 4) {
            _$d9(_$l1, _$pY);
            _$ei |= 4096;
        }
        _$pY = _$zT(_$wC("$_JQnh"));
        if (_$pY && _$pY["length"] === 4) {
            _$d9(_$l1, _$pY);
            _$ei |= 8192;
        }
    } catch (_$ff) {}
    if (_$eH != _$u4 && _$gq != _$u4 && _$xv != _$u4) try {
        _$d9(_$l1, _$co(0, 360, _$eH));
        _$d9(_$l1, _$co(-180, 180, _$gq));
        _$d9(_$l1, _$co(-90, 90, _$xv));
        _$ei |= 16384;
    } catch (_$ff) {}
    if (_$rs != _$u4) {
        var _$vI = window["Math"]["round"]((_$rs + (_$uf ? _$ws() - _$eT : 0)) / 100.0);
        _$d9(_$l1, _$pS(_$vI));
        _$ei |= 32768;
    }
    var _$kc = [];
    _$bb([_$ei], _$kc);
    for (var _$i2 = 0; _$i2 < 4; ++_$i2) _$l1[2 + _$i2] = _$kc[_$i2];
    return _$l1;
}

function _$sJ() {
    var _$nd = document["getElementsByTagName"]("script");
    var _$i2 = _$nd[_$nd["length"] - 1];
    _$i2["parentNode"]["removeChild"](_$i2);
}


function _$wa(_$nd) {
    var _$i2 = window["ActiveXObject"];
    if (_$i2) {
        var _$pY = ["ShockwaveFlash.ShockwaveFlash", "AcroPDF.PDF", "PDF.PdfCtrl", "QuickTime.QuickTime", "rmocx.RealPlayer G2 Control", "rmocx.RealPlayer G2 Control.1", "RealPlayer.RealPlayer(tm) ActiveX Control (32-bit)", "RealVideo.RealVideo(tm) ActiveX Control (32-bit)", "RealPlayer", "SWCtl.SWCtl", "WMPlayer.OCX", "AgControl.AgControl", "Skype.Detection"];
        for (var _$ei = 0; _$ei < _$pY["length"]; _$ei++) try {
            new _$i2(_$pY[_$ei]);
            _$nd.push(_$pY[_$ei]);
        } catch (_$l1) { return null; }
    }
};

function _$nS(_$nd, _$i2) { return _$zQ(_$eJ(_$nd, _$i2)); };

function _$s0(_$nd, _$i2) {
    var _$pY = [],
        _$ei;
    for (_$ei = 0; _$ei < 16; _$ei++) _$pY.push(_$nd[_$ei] ^ _$i2[_$ei]);
    return _$pY;
};

function _$cX(_$nd, _$i2) { return _$nd[_$i2]; }


function _$u6(_$nd, _$i2) { if (_$i2) _$nd += '?' + _$i2; return _$nd; }

function _$rr(_$nd) { window["$b_callHandler"]("Z8XHj", '', _$nd); }

function _$uM(_$nd) { return _$zP(_$vi(_$nd)); }


function _$uc(_$nd) { if (typeof _$nd === "string") _$nd = _$jg(_$nd); var _$i2 = _$ds(function() { return _$xq; }); var _$pY = window[_$i2] || (window[_$i2] = _$mu()); var _$ei = 0; for (var _$l1 = 0; _$l1 < _$nd["length"]; _$l1++) _$ei = _$pY[(_$ei ^ _$nd[_$l1]) & 0xFF]; return _$ei; }

function _$v8(_$nd) {
    var _$i2 = _$sL(_$nd);
    var _$pY = '';
    if (_$i2._$xY === 1) _$pY = _$dq(_$i2._$xX);
    else if (_$i2._$xY === 2) _$pY = _$i2._$xX;
    else if (_$i2._$xY === 3) return _$nd;
    var _$ei = _$oY(decodeURIComponent(_$pY["replace"](/\+/g, "%20")));
    _$pY = _$s9(_$pY, '#');
    var _$l1 = _$pY[1];
    if (_$pY[0]["indexOf"]('?') === -1) _$pY = _$pY[0] + '?';
    else _$pY = _$pY[0] + '&';
    var _$ta = _$i2._$zj + _$pY;
    _$ta += _$kB(_$nd, _$ei);
    _$ta += _$l1;
    return _$ta;
}

function _$bd() { _$fS(); }
function _$tF(_$nd) { var _$i2 = [0, 1, 3, 7, 0xf, 0x1f]; return (_$nd >> _$gG) | ((_$nd & _$i2[_$gG]) << (6 - _$gG)); }


function _$ds(_$nd) { return _$nd["toString"]()["match"](/{\s*return\s*([A-Za-z0-9$_-]+);?\s*}/)[1]; }


function _$ud(_$nd, _$i2) { if (typeof _$nd === "string") _$nd = _$jg(_$nd); var _$pY = _$gi(_$nd, _$i2); return _$zQ(_$pY); }
function _$mu() {
    var _$nd = [];
    for (var _$i2 = 0; _$i2 < 256; ++_$i2) {
        var _$pY = _$i2;
        for (var _$ei = 0; _$ei < 8; ++_$ei)
            if ((_$pY & 0x80) !== 0) _$pY = (_$pY << 1) ^ 7;
            else _$pY <<= 1;
        _$nd[_$i2] = _$pY & 0xff;
    }
    return _$nd;
}
function _$vp(_$nd, _$i2, _$pY) { if (_$nd !== _$i2) { if (localStorage && localStorage.$d === '1') debugger; if (!_$pY) _$pY = "assert failed: " + _$nd + " is not same as " + _$i2; throw _$pY; } }
function _$s9(_$nd, _$i2) { var _$pY = _$nd["indexOf"](_$i2); if (_$pY === -1) return [_$nd, '']; return [_$nd["substr"](0, _$pY), _$nd["substr"](_$pY)]; }
function _$jv(_$nd) { return new _$w4()._$wV(_$nd)._$wr(); }

function _$ja(_$nd, _$i2) { document["cookie"] = _$nd + '=' + _$i2 + "; path=/" + _$wL(365 * 10); }

function _$fS() {
    _$vV(document, "mousedown", _$sl);
    _$vV(document, "mouseup", _$aH);
    _$vV(document, "mousemove", _$iH);
    _$vV(document, "keydown", _$wW);
    _$vV(document, "touchstart", _$v9);
    _$vV(document, "touchmove", _$vA);
    _$vV(document, "touchend", _$vQ);
    _$vV(document, "click", _$rg);
    _$vV(document, "input", _$xC);
    _$vV(document, "scroll", _$uz);
    _$vV(window, "load", _$pf);
    if (document["addEventListener"]) {
        _$vV(document, "driver-evaluate", _$pf);
        _$vV(document, "webdriver-evaluate", _$pf);
        _$vV(document, "selenium-evaluate", _$pf);
    }
    _$vV(window, "error", _$bC);
    _$vV(window, "load", _$gP);
    window["setInterval"](function() { _$dW(10); }, 50000);
    try {
        if (window["DeviceMotionEvent"] != _$u4) {
            _$xD = 0;
            window["addEventListener"]("devicemotion", _$xe, true);
        }
        if (window["DeviceOrientationEvent"] != _$u4) {
            _$t1 = 0;
            window["addEventListener"]("deviceorientation", _$aN, true);
        }
    } catch (_$nd) {}
    _$pk();
    _$vV(window, "load", function() {
        _$aA = _$ws();
        _$eT = _$ws();
        _$xj();
    });
    _$ah();
    _$qq();
    try { var _$i2 = _$wC("$_fpn1"); if (!_$i2) { _$i2 = _$vi(27); if (_$i2) _$vs("$_fpn1", _$i2); } } catch (_$nd) {}
    window["$b_onBridgeReady"](function() {
        _$rr(function(_$pY) {
            try {
                _$vs("$_fpn1", _$pY);
                _$dW(8);
            } catch (_$ei) {}
        });
    });
    _$rv();
}
function _$ly() { var _$nd = _$zT(_$vi(19) + _$c8[0] + _$to(function() { return _$ea; })); return _$wh(_$nd); }

function _$qI(_$nd, _$i2) { return _$nd["tagName"]["toLowerCase"]() == _$i2; }

function _$to(_$nd) {
    var _$i2 = _$ds(_$nd);
    if (_$gK(_$i2, "_$")) _$i2 = _$i2["substr"](2)["replace"]('$', '.');
    else _$i2 = '';
    return _$i2;
}

function _$sp() {
    try { var _$nd = document["createElement"]("canvas"); var _$i2 = _$nd["getContext"]("webgl") || _$nd["getContext"]("experimental-webgl"); } catch (_$pY) {; return; };

    function _$l1() {
        var _$gL = _$i2["getSupportedExtensions"]();
        for (var _$s4 = 0; _$s4 < _$gL["length"]; _$s4++) {
            var _$bX = _$gL[_$s4];
            var _$t6 = _$i2["getExtension"](_$bX);
            _$ta.push(_$bX);
            _$ei(_$t6);
        }
    }
    try {
        var _$ta = [];
        var _$qm = "attribute vec2 attrVertex;varying vec2 varyinTexCoordinate;uniform vec2 uniformOffset;void main(){varyinTexCoordinate=attrVertex+uniformOffset;gl_Position=vec4(attrVertex,0,1);}";
        var _$eB = "precision mediump float;varying vec2 varyinTexCoordinate;void main() {gl_FragColor=vec4(varyinTexCoordinate,0,1);}";
        var _$lg = _$i2["createBuffer"]();
        _$i2["bindBuffer"](_$i2["ARRAY_BUFFER"], _$lg);
        var _$ff = new window["Float32Array"]([-.2, -.9, 0, .4, -.26, 0, 0, .813264543, 0]);
        _$i2["bufferData"](_$i2["ARRAY_BUFFER"], _$ff, _$i2["STATIC_DRAW"]);
        _$lg["itemSize"] = 3;
        _$lg["numItems"] = 3;
        var _$xs = _$i2["createProgram"](),
            _$vI = _$i2["createShader"](_$i2["VERTEX_SHADER"]);
        _$i2["shaderSource"](_$vI, _$qm);
        _$i2["compileShader"](_$vI);
        var _$kc = _$i2["createShader"](_$i2["FRAGMENT_SHADER"]);
        _$i2["shaderSource"](_$kc, _$eB);
        _$i2["compileShader"](_$kc);
        _$i2["attachShader"](_$xs, _$vI);
        _$i2["attachShader"](_$xs, _$kc);
        _$i2["linkProgram"](_$xs);
        _$i2["useProgram"](_$xs);
        _$xs["vertexPosAttrib"] = _$i2["getAttribLocation"](_$xs, "attrVertex");
        _$xs["offsetUniform"] = _$i2["getUniformLocation"](_$xs, "uniformOffset");
        _$i2["enableVertexAttribArray"](_$xs["vertexPosArray"]);
        _$i2["vertexAttribPointer"](_$xs["vertexPosAttrib"], _$lg["itemSize"], _$i2["FLOAT"], !1, 0, 0);
        _$i2["uniform2f"](_$xs["offsetUniform"], 1, 1);
        _$i2["drawArrays"](_$i2["TRIANGLE_STRIP"], 0, _$lg["numItems"]);
        if (_$i2["canvas"] != null) _$ta.push(_$i2["canvas"]["toDataURL"]());
        _$l1();
        _$ei(_$i2);
        if (_$i2["getShaderPrecisionFormat"]) {
            var _$bW = [_$i2["VERTEX_SHADER"], _$i2["FRAGMENT_SHADER"]],
                _$sK = [_$i2["HIGH_FLOAT"], _$i2["MEDIUM_FLOAT"], _$i2["LOW_FLOAT"], _$i2["HIGH_INT"], _$i2["MEDIUM_INT"], _$i2["LOW_INT"]];
            for (var _$dE = 0; _$dE < _$bW["length"]; _$dE++)
                for (var _$f3 = 0; _$f3 < _$sK["length"]; _$f3++) {
                    var _$nI = _$i2["getShaderPrecisionFormat"](_$bW[_$dE], _$sK[_$f3]);
                    _$ta.push(_$nI["rangeMin"], _$nI["rangeMax"], _$nI["precision"]);
                }
        }
    } catch (_$pY) {; };

    function _$ei(_$gL) {
        for (var _$s4 in _$gL)
            if (_$s4["toUpperCase"]() === _$s4) {
                var _$bX = _$i2["getParameter"](_$gL[_$s4]);
                if (_$bX != _$u4) {
                    if (typeof _$bX === "number" && _$bX >= 0xFFFFFF) continue;
                    _$ta.push(_$bX);
                }
            }
    };
    return _$zQ(_$jv(_$ta.join(':')));
}

function _$bJ() { return window["location"]; }

function _$kB(_$nd, _$i2) {
    var _$pY = [];
    var _$ei = _$wY(6);
    if (_$ei) {
        _$pY = _$pY["concat"](_$i2);
        _$pY.push(_$tL(_$nd) ? 1 : 0);
        var _$l1 = _$vW + _$ei + _$xT(_$pY);
        _$l1 += _$sy(_$l1);
        return _$zF + '=' + _$l1;
    } else return _$zF + '=';
}

function _$u9() {
    var _$nd;
    try { _$nd = new window["ActiveXObject"]("ShockwaveFlash.ShockwaveFlash"); } catch (_$i2) {
        var _$pY = window["navigator"]["mimeTypes"];
        _$nd = _$pY["application/x-shockwave-flash"];
        _$nd = _$nd && _$nd["enabledPlugin"];
    }
    return _$nd !== _$u4;
}

function _$tD(_$nd) {
    var _$i2 = _$nd.split('');
    _$uA(_$i2, 0, _$i2.length, 2);
    return _$i2.join('');
}

function _$uA(_$nd, _$i2, _$pY, _$ei) {
    var _$l1 = Math.floor((_$i2 + _$pY) / 2);
    if (_$ei > 0) { _$ei--; if (_$l1 - _$i2 >= 3) _$uA(_$nd, _$i2, _$l1, _$ei); if (_$pY - _$l1 >= 3) _$uA(_$nd, _$l1, _$pY, _$ei); }
    for (var _$ta = _$i2; _$ta < _$l1; _$ta += 2) {
        var _$qm = _$nd[_$ta];
        var _$eB = _$pY - 1 - (_$ta - _$i2);
        _$nd[_$ta] = _$nd[_$eB];
        _$nd[_$eB] = _$qm;
    }
}

// _$gb()主要是加工网页元素id为“9DhefwqGPrzGxEp9hPaoag”的函数
function _$gb() {
    var _$nd = document["getElementById"]("9DhefwqGPrzGxEp9hPaoag");

    function _$eB() {
        var _$lg, _$ff;
        _$lg = _$dN(_$i2["charAt"](_$ei));
        if (_$lg < 0) {;
            _$ei++;
            _$ff = _$ei + 3;
            _$lg = 0;
            for (; _$ei < _$ff; _$ei++) _$lg = _$lg * 86 + _$dN(_$i2["charAt"](_$ei));
        } else if (_$lg < 64) _$ei++;
        else if (_$lg <= 86) {
            _$lg = (_$lg - 64) * 86 + _$dN(_$i2["charAt"](_$ei + 1)) + 64;
            _$ei += 2;
        } else;
        return _$lg;
    }
    var _$i2 = _$nd["content"];
    // _$nd["parentElement"]["removeChild"](_$nd); //这句话把9DhefwqGPrzGxEp9hPaoag元素删除了，先注释掉，便于调试
    var _$pY = _$i2["length"],
        _$ei = 0,
        _$l1, _$ta = 0;
    var _$qm = _$eB();
    _$v4 = _$aK(_$v4);
    _$gG = _$aK(_$gG);
    _$vf = new window["Array"](_$qm);
    while (_$ei < _$pY) {
        _$l1 = _$eB();
        _$vf[_$ta] = _$i2["substr"](_$ei, _$l1);
        _$ei += _$l1;
        _$ta++;
    };
}
function _$vV(_$nd, _$i2, _$pY) {
    if (_$nd["addEventListener"]) _$nd["addEventListener"](_$i2, _$pY);
    else {
        _$i2 = "on" + _$i2;
        _$nd["attachEvent"](_$i2, _$pY);
    }
}
function _$iH(_$nd) {
    if (_$yn["length"] < 1000) _$yn.push(_$nd["offsetX"], _$nd["offsetY"], _$nd.x, _$nd.y);
    _$bH++;
}
function _$jn(_$nd) {
    _$nd = _$nd["split"]("`");
    if (_$nd["length"] === 4)
        if (localStorage) {
            localStorage["$_turi"] = _$nd[0];
            localStorage["$_ttarg"] = _$nd[1];
            localStorage["$_tk1"] = _$nd[2];
            localStorage["$_tk2"] = _$nd[3];
        }
}
function _$vz() {
    var _$nd;
    var _$i2 = window["navigator"];
    var _$pY = _$i2["connection"] || _$i2["mozConnection"] || _$i2["webkitConnection"];
    if (_$pY)
        if (_$pY["type"] == "bluetooth") _$nd = 1;
        else if (_$pY["type"] == "cellular") _$nd = 2;
    else if (_$pY["type"] == "ethernet") _$nd = 3;
    else if (_$pY["type"] == "wifi") _$nd = 4;
    else if (_$pY["type"] == "wimax") _$nd = 5;
    else _$nd = 0;
    return _$nd;
}
function _$c6() { return window["Math"]["ceil"](_$ws() / 1000); }

function _$wL(_$nd) { var _$i2 = _$ws() + _$nd * 24 * 60 * 60 * 1000; return "; expires=" + new Date(_$i2)["toGMTString"](); }

function _$j4(_$nd, _$i2, _$pY) {
    _$aZ(2, _$xp(5));
    if (_$pY && (_$jd & 8) && _$nd && _$nd["length"] > 0) {
        var _$ei = _$c4(_$i2)[1];
        _$nd = _$wN(_$nd, _$ei);
    }
    return _$nd;
}
function _$xp(_$nd) {
    var _$i2 = window.Error && new window.Error();
    if (_$i2) {
        var _$pY = _$i2["stack"];
        if (!_$pY) return;
        var _$ei = _$pY["toString"]();
        var _$l1 = _$ei["split"]('\n');
        _$ei = _$l1["pop"]();
        if (_$ei === '' && _$l1["length"] > 0) _$ei = _$l1["pop"]();
        if (_$ei["indexOf"]("Object.InjectedScript.evaluate") !== -1 || _$gK(_$ei, "@debugger") || _$ei === "evaluate") { _$wd(_$nd, 1); return true; }
    }
}
function _$jo(_$nd) {
    var _$i2;
    var _$pY = function() { _$nd(true); };
    var _$ei = function() { _$nd(false); };
    try {
        var _$l1 = window["navigator"];
        if (window["webkitRequestFileSystem"] && !(_$l1["appVersion"] && /Android 4\.[0-3].+ (GT|SM|SCH)-/ ["test"](_$l1["appVersion"]))) window["webkitRequestFileSystem"](window["TEMPORARY"], 1, _$ei, _$pY);
        else if ("MozAppearance" in document["documentElement"]["style"]) {
            _$i2 = window["indexedDB"]["open"]("EkcP");
            _$i2["onerror"] = _$pY;
            _$i2["onsuccess"] = _$ei;
        } else if (window["safari"] && window["safari"]["pushNotification"]) try { window["localStorage"]["length"] ? _$ei() : (window["localStorage"].x = 1, window["localStorage"]["removeItem"]("x"), _$ei()); } catch (_$ta) { _$pY(); } else if (!window["indexedDB"] && (window["PointerEvent"] || window["MSPointerEvent"])) _$pY();
            else _$ei();
    } catch (_$ta) { _$ei(); }
}
function _$oY(_$nd) { return new _$w4()._$wV(_$nd)._$wr()["slice"](0, 16); }

function _$hn() {
    var _$nd = _$zT(_$vi(21) + _$c8[2] + _$to(function() { return _$S9; }));
    _$s8(4096, _$nd["length"] !== 32);
    _$vp(_$nd["length"], 32, "Stolen Via Net: Cookie key length is incorrect.");
    return _$wh(_$nd);
}

function _$zH(_$nd) {
    if (window["JSON"] && window["JSON"]["stringify"]) return JSON["stringify"](_$nd);

    function _$pY(_$ei) {
        var _$l1, _$ta, _$qm;
        switch (typeof _$ei) {
            case "string":
                return _$i2(_$ei);
            case "number":
                return isFinite(_$ei) ? String(_$ei) : "null";
            case "boolean":
            case "null":
                return String(_$ei);
            case "object":
                if (!_$ei) return "null";
                var _$eB = Object["prototype"]["toString"]["apply"](_$ei);
                _$qm = [];
                if (_$eB === "[object Array]") { for (_$l1 = 0; _$l1 < _$ei["length"]; _$l1 += 1) _$qm[_$l1] = _$pY(_$ei[_$l1]); return '[' + _$qm.join(',') + ']'; }
                for (_$ta in _$ei)
                    if (Object["prototype"]["hasOwnProperty"]["call"](_$ei, _$ta)) _$qm.push(_$i2(_$ta) + ':' + _$pY(_$ei[_$ta]));
                return '{' + _$qm.join(',') + '}';
        }
    }
    return _$pY(_$nd);

    function _$i2(_$ei) { var _$l1 = /[\\\"\u0000-\u001f\u007f-\u009f\u00ad\u0600-\u0604\u070f\u17b4\u17b5\u200c-\u200f\u2028-\u202f\u2060-\u206f\ufeff\ufff0-\uffff]/g; var _$ta = { '\b': '\\b', '\t': '\\t', '\n': '\\n', '\f': '\\f', '\r': '\\r', '"': '\\"', '\\': '\\\\' }; return '"' + _$ei["replace"](_$l1, function(_$qm) { var _$eB = _$ta[_$qm]; return _$eB ? _$eB : '\\u' + ("0000" + _$qm["charCodeAt"](0)["toString"](16))["slice"](-4); }) + '"'; }
}

function _$cI() {
    if (!localStorage) return;
    if (localStorage["$_ck"]) {
        var _$nd = localStorage["$_ck"];
        var _$i2 = _$vi(6);
        if (_$nd == _$i2) return;
        _$s8(16384);
    } else { _$s8(32768); }
}
function _$vy(a, b, c) { var d = []; for (var e = 0; e < c["length"]; e++) d[e] = "c[" + e + ']'; return eval("a[b](" + d.join(',') + ')'); }

function _$rg(_$nd) { _$dW(3);++_$yl; }

function _$aZ(_$nd, _$i2) { _$hT |= _$nd; if (_$i2) _$ps |= _$nd; }

function _$qY() {
    if (!localStorage) { _$dW(1); return; }
    var _$nd = _$uM(5);
    if (_$nd) {
        var _$i2 = _$fN(_$zy);
        _$ja(_$i2, _$nd);
        localStorage["$_ck"] = _$vi(6);
    } else _$cI();
}
function _$oG(_$nd, _$i2) {
    var _$pY = _$ps;
    _$s8(_$nd);
    if ((_$pY & 134217728) && _$bZ) return;
    else _$bZ = _$i2;
}
function _$cr() {
    var _$nd = document["getElementsByTagName"]("base");
    if (_$nd && _$nd["length"] > 0 && _$nd[_$nd["length"] - 1]["href"]) {
        var _$i2 = document["createElement"]('a');
        _$i2["href"] = _$nd[_$nd["length"] - 1]["href"];
        return _$i2["pathname"];
    } else return _$vu;
}
function _$iV(_$nd) {
    var _$i2 = _$nd["length"],
        _$pY = new Array(_$i2),
        _$ei, _$l1;
    for (_$ei = 0; _$ei < _$i2; _$ei++) {
        _$l1 = _$nd["charCodeAt"](_$ei);
        if (_$l1 >= 40 && _$l1 < 126) _$pY[_$ei] = String.fromCharCode(_$l1 + 1);
        else if (_$l1 === 126) _$pY[_$ei] = '(';
        else _$pY[_$ei] = _$nd["charAt"](_$ei);
    }
    return _$pY.join('');
}
function _$vt() {
    var _$nd, _$i2 = [];
    for (var _$pY = 0; _$pY < 256; _$pY++) {
        _$nd = _$pY;
        for (var _$ei = 0; _$ei < 8; _$ei++) _$nd = ((_$nd & 1) ? (0xEDB88320 ^ (_$nd >>> 1)) : (_$nd >>> 1));
        _$i2[_$pY] = _$nd;
    }
    return _$i2;
}
function _$fs(_$nd, _$i2, _$pY, _$ei) {
    if (_$i2 == '=') return _$nd[_$pY] = _$ei;
    else if (_$i2 == "+=") return _$nd[_$pY] += _$ei;
}

function _$h5(_$nd, _$i2) {
    var _$pY = [],
        _$ei;
    for (_$ei = 0; _$ei < 2; _$ei++) _$pY.push(_$nd[_$ei] ^ _$i2[_$ei]);
    return _$pY;
}

function _$d9(_$nd, _$i2) { for (var _$pY = 0; _$pY < _$i2["length"]; _$pY++) _$nd.push(_$i2[_$pY]); }

function _$xC(_$nd) {++_$yu; }

function _$ws() { return new Date()["getTime"](); }

function _$vd(_$nd, _$i2) {
    var _$pY = [];
    for (var _$ei = 2; _$ei < arguments["length"]; _$ei++) _$pY.push(arguments[_$ei]);
    if ("submit" == _$i2)
        if (_$sT(_$nd) && _$di(_$nd["tagName"], "form")) return _$nd[_$i2]["apply"](_$nd, _$pY);
        else if (_$pY["length"] === 0 && _$nd && _$nd["length"] == 1 && _$nd["jquery"] && _$sT(_$nd[0]) && _$qI(_$nd[0], "form")) return _$nd[_$i2]["apply"](_$nd, _$pY);
    else return _$xP(_$nd, _$i2, _$pY);
    return _$nd[_$i2]["apply"](_$nd, _$pY);
}

function _$uK(_$nd) { var _$i2 = []; for (var _$pY = 1; _$pY < arguments["length"]; _$pY++) _$i2.push(arguments[_$pY]); return _$nd["apply"](_$i2); }

function _$ey(_$nd) { return unescape(encodeURIComponent(_$nd)); }

function _$ro(_$nd, _$i2) {
    _$i2 = _$i2["split"](',');
    for (var _$pY = 0; _$pY < _$i2["length"]; _$pY++)
        if (_$nd[_$i2[_$pY]] !== _$u4) return 1;
}

function _$eJ(_$nd, _$i2) { if (typeof _$nd === "string") _$nd = _$jg(_$nd); var _$pY = new _$um(_$i2, true); return _$pY._$uw(_$nd, true); }

function _$lw(_$nd, _$i2) {
    _$nd = _$nd.split('`');
    _$i2 = _$lT(_$i2, 2);
    var _$pY = String.fromCharCode(95, 36);
    for (var _$ei = 0; _$ei < _$i2.length; _$ei++) _$i2[_$ei] = _$pY + _$i2[_$ei];
    var _$l1 = [String.fromCharCode(118, 97, 114, 32)];
    for (var _$ei = 0; _$ei < _$nd.length; _$ei++) {
        if (_$ei > 0) _$l1.push(',');
        _$l1.push(_$i2[_$ei] + '="' + _$nd[_$ei] + '"');
    }
    _$l1.push(';');
    return _$l1.join('');
}

function _$tt(_$nd) { _$nd = _$it(_$it(_$nd, '#')[0], '?')[0]; return _$nd["substr"](0, _$nd["lastIndexOf"]('/') + 1); }

function _$rY(_$nd, _$i2, _$pY) {
    _$i2 = _$i2 || 0;
    if (_$pY === _$u4) _$pY = _$nd.length;
    var _$ei = [],
        _$l1;
    while (true) {
        _$l1 = _$i2 + 40960;
        if (_$l1 >= _$pY) { _$ei.push(String.fromCharCode.apply(null, _$nd.slice(_$i2, _$pY))); break; } else {
            _$ei.push(String.fromCharCode.apply(null, _$nd.slice(_$i2, _$l1)));
            _$i2 = _$l1;
        }
    }
    return _$ei.join('');
}

function _$gi(_$nd, _$i2) {;
    _$i2 = _$xO(_$i2);
    var _$pY = Math["floor"](_$nd["length"] / 8),
        _$ei, _$l1 = [],
        _$ta = [],
        _$qm = 8 - (_$nd["length"] % 8),
        _$eB;
    _$eB = _$xO(_$e4(8));
    _$ta = _$eB["slice"](0);
    for (_$ei = 0; _$ei < _$pY; _$ei++) _$l1.push(_$xO(_$nd["slice"](_$ei * 8, _$ei * 8 + 8)));
    var _$lg = _$nd["slice"](_$pY * 8);
    for (_$ei = 0; _$ei < _$qm; _$ei++) _$lg.push(_$qm);
    _$l1.push(_$xO(_$lg));
    for (_$ei = 0; _$ei < _$l1["length"]; _$ei++) {
        _$iU(_$h5(_$l1[_$ei], _$eB), _$ta, _$i2);
        _$eB = _$ta["slice"](_$ta["length"] - 2);
    }
    var _$ff = [];
    _$bb(_$ta, _$ff);
    return _$ff;
}

function _$y3(_$nd) {
    var _$i2 = _$zT(_$nd),
        _$pY = (_$i2[0] << 8) + _$i2[1],
        _$ei = _$i2["length"],
        _$l1;
    for (_$l1 = 2; _$l1 < _$ei; _$l1 += 2) {
        _$i2[_$l1] ^= (_$pY >> 8) & 0xFF;
        if (_$l1 + 1 < _$ei) _$i2[_$l1 + 1] ^= _$pY & 0xFF;
        _$pY++;
    }
    return _$i2["slice"](2);
}

function _$wx() { if ("1" == _$vi(24)) window["setInterval"](_$bp, 2000); }

function _$pS(_$nd) { _$nd = window["Math"]["round"](_$nd); return [((_$nd & 0xFF00) >> 8), (_$nd & 0xFF)]; }

function _$wt() {;

    function _$nd(_$kc, _$bW, _$sK) { _$bW = _$bW["split"](','); for (var _$dE = 0; _$dE < _$bW["length"]; _$dE++) _$sK.push(_$kc[_$bW[_$dE]] || 0); }
    var _$i2 = [],
        _$pY, _$ei, _$l1;
    var _$ta = window["navigator"];
    for (_$pY in _$ta) { try { _$l1 = _$ta["hasOwnProperty"](_$pY); } catch (_$qm) { _$l1 = false; } if (_$l1) { _$i2.push(_$pY); if (_$pY !== "appVersion" && _$pY !== "userAgent") { _$ei = _$ta[_$pY]; if (typeof _$ei !== "object") _$i2.push(_$ei); } } }
    _$i2.push((_$ta["languages"] || []).join(','));
    var _$eB = _$ta["plugins"];
    if (_$eB)
        for (_$pY = 0; _$pY < _$eB["length"]; _$pY++) {
            _$ei = _$eB[_$pY];
            if (_$ei["name"]) _$i2.push(_$ei["name"]);
            else if (_$ei["filename"]) _$i2.push(_$ei["filename"]);
        }
    _$wa(_$i2);
    var _$lg = _$ta["mimeTypes"];
    if (_$lg)
        for (_$pY = 0; _$pY < _$lg["length"]; _$pY++) {
            _$ei = _$lg[_$pY];
            if (_$ei["type"]) _$i2.push(_$ei["type"]);
            else if (_$ei["description"]) _$i2.push(_$ei["description"]);
        }
    var _$ff = window["screen"];
    var _$xs = "width,height,pixelDepth,colorDepth";
    _$xs = _$xs["split"](',');
    for (_$pY = 0; _$pY < _$xs["length"]; _$pY++)
        if (typeof _$ff[_$xs[_$pY]] === "number") _$i2.push(_$ff[_$xs[_$pY]]);
    _$i2.push(new Date()["getTimezoneOffset"]());
    var _$vI = "safari,ontouchstart,sidebar,localStorage,clipboardData,sessionStorage,indexedDB,openDatabase,standalone,$PreUCBrowserClassic,UCBrowserMessageCenter,__firefox__,_firefox_ReaderMode,__mttCreateFrame,mttCustomJS,__crWeb,__gCrWeb,MicroMessenger,SogouMse,ucweb,qb_bridge,FaveIconJavaInterface,jesion,dophin,orientation";
    _$vI = _$vI["split"](',');
    for (_$pY = 0; _$pY < _$vI["length"]; _$pY++) _$i2.push(window[_$vI[_$pY]] !== _$u4 ? 1 : 0);
    _$ei = _$wC("$_f0", _$vb);
    if (_$ei) _$i2.push(_$ei);
    _$ei = _$wC("$_f1", _$sp);
    if (_$ei) _$i2.push(_$ei);
    _$ei = _$wC("$_fh0");
    if (_$ei) _$i2.push(_$ei);
    return _$jv(_$i2.join(':'));
}

function _$pf() {
    var _$nd = 0,
        _$i2 = "_Selenium_IDE_Recorder,_selenium,callSelenium",
        _$pY = "__driver_evaluate,__webdriver_evaluate,__selenium_evaluate,__fxdriver_evaluate,__driver_unwrapped,__webdriver_unwrapped,__selenium_unwrapped,__fxdriver_unwrapped,__webdriver_script_func,__webdriver_script_fn",
        _$ei = ["selenium", "webdriver", "driver"];
    try {
        _$nd = _$ro(window, _$i2) || _$ro(document, _$pY);
        for (var _$l1 in document)
            if (_$l1[0] === '$' && _$l1["match"]('^\\$[a-z]dc_') && document[_$l1]["cache_"]) _$nd = 1;
        for (var _$ta = 0; _$ta < _$ei["length"]; _$ta++)
            if (document["documentElement"]["getAttribute"](_$ei[_$ta])) _$nd = 1;
    } catch (_$qm) {; }
    if (_$nd) {
        window._$y1 = 1;
        _$oG(134217728, 31);
    }
}

function _$t3() {
    _$xS = "qrcklmDoExthWJiHAp1sVYKU3RFMQw8IGfPO92bvLNj.7zXBaSnu0TC6gy_4Ze5d";
    _$xS = _$xS["split"]('');
    _$wl = window["document"];
    _$b1 = top["location"];
    if (opener) _$jM = opener["location"];
    else _$jM = null;
    _$pP = window["Math"]["random"];
    _$us = window["setTimeout"];
    _$ue = window["setInterval"];
    _$zZ = window["$_ts"];
    localStorage = window["localStorage"];
    if (localStorage) try {
        localStorage["___ts___"] = "___ts___";
        localStorage["removeItem"]("___ts___");
        localStorage["__#classType"] = "localStorage";
    } catch (_$nd) { localStorage = _$u4; }
    if (!_$hT && !_$ps) {
        _$ps = 0;
        _$hT = 0;
        _$xg = 0;
    }
    window["console"] = window["console"] || (function() {
        var _$i2 = {};
        _$i2["log"] = function() {};
        return _$i2;
    })();
    if (!_$zZ) {
        _$zZ = new Object();
        window["$_ts"] = _$zZ;
    }
    _$uG = _$zT("wP3dxhyJgpbC6tVm_ewcCO");
}

function _$db(_$nd) {
    var _$i2 = Number(_$vi(23)) / 1000;
    var _$pY = _$d1() / 1000;
    if (!(_$vD & 64) || _$pY - _$i2 >= 60 || (_$ps & 134217728)) _$nd += "&T=" + _$wY(11);
    var _$ei = document["createElement"]("script");
    _$ei["setAttribute"]("src", "/4QbVtADbnLVIc/jW39ezbWPr.js?" + _$nd);
    document["body"]["appendChild"](_$ei);
    _$ei["onload"] = _$ei["onreadystatechange"] = function() {
        if (!this["readyState"] || this["readyState"] === "loaded" || this["readyState"] === "complete") {
            _$ei["parentNode"]["removeChild"](_$ei);
            _$ei["onload"] = _$ei["onreadystatechange"] = null;
        }
    };
}

function _$dN(_$nd) { return _$zE[_$nd["charCodeAt"](0)]; }

function _$c0(_$nd, _$i2) {
    _$nd = "FSSBB" + _$nd;
    if (typeof _$i2 === "object") _$i2 = _$zH(_$i2);
    _$i2 = _$iV(_$i2["toString"]());
    if (_$i2["length"] > 16 || _$i2["indexOf"](';') !== -1) _$i2 = _$zQ(_$oY(_$i2));
    if (localStorage) {
        var _$pY = parseInt(_$ws() / (1000 * 60 * 60));
        var _$ei = localStorage[_$nd];
        if (_$ei) { _$ei = _$it(_$ei, ':'); if (_$ei["length"] === 2 && _$ei[1] === _$i2 && _$pY - _$ei[0] < 24) {; return true; } }
        localStorage[_$nd] = _$pY + ':' + _$i2;
    }
}

function _$wZ(_$nd) { if (typeof _$nd === "string") _$nd = _$jg(_$nd); var _$i2 = _$ds(function() { return _$hs; }); var _$pY = window[_$i2] || (window[_$i2] = _$vt()); var _$ei = 0 ^ (-1); for (var _$l1 = 0; _$l1 < _$nd["length"]; _$l1++) _$ei = (_$ei >>> 8) ^ _$pY[(_$ei ^ _$nd[_$l1]) & 0xFF]; return (_$ei ^ (-1)) >>> 0; }

function _$wh(_$nd) {
    var _$i2 = window["Math"]["ceil"](window["Math"]["random"]() * 256);
    _$bb([_$c6()], _$nd);
    for (var _$pY = 0; _$pY < _$nd["length"]; _$pY++) _$nd[_$pY] ^= _$i2;
    _$nd.push(_$i2);
    return _$nd;
}

function _$pk() {
    var _$nd = window["navigator"];

    function _$pY(_$ei) {
        _$a8 = parseInt(_$ei["level"] * 100);
        _$bN = _$ei["charging"];
        if (_$ei["chargingTime"] === window["Infinity"]) _$vE = 0;
        else _$vE = parseInt(_$ei["chargingTime"]);
    }
    try {
        if (_$nd["battery"]) _$pY(_$nd["battery"]);
        else if (_$nd["getBattery"]) _$nd["getBattery"]()["then"](_$pY);
        else return;
    } catch (_$i2) {}
}

function _$vB() {
    var _$nd = 3,
        _$i2 = document["createElement"]("div"),
        _$pY = _$i2["getElementsByTagName"]('i');
    while (_$i2["innerHTML"] = "<!--[if gt IE " + (++_$nd) + "]><i></i><![endif]-->", _$pY[0]);
    if (_$nd > 4) return _$nd;
    if (window["eval"]("/*@cc_on!@*/false")) return 10;
    try { if (new window["ActiveXObject"]("Microsoft.XMLHTTP") ? true : false) return 11; } catch (_$ei) {}
}

function _$it(_$nd, _$i2) { var _$pY = _$nd["indexOf"](_$i2); if (_$pY === -1) return [_$nd]; return [_$nd["substr"](0, _$pY), _$nd["substr"](_$pY + 1)]; }

function _$eK() {
    for (var _$nd in window)
        if (_$gK(_$nd, "WebXMLogMsg_UNIQUE_")) return 1;
}

function _$v9(_$nd) {
    _$yo++;
    _$oN = _$ws();
    _$xk(_$nd);
    _$dW(4);
}

function _$di(_$nd, _$i2) { return typeof _$nd == "string" && typeof _$i2 == "string" && _$nd["toLowerCase"]() === _$i2["toLowerCase"](); }

function _$aK(_$nd, _$i2) { if (_$nd) { _$nd = parseInt(_$nd); if (!window["isNaN"](_$nd)) return _$nd; } if (arguments["length"] > 1) return _$i2; return window["NaN"]; }

function _$aL(_$nd) {
    var _$i2 = "/",
        _$pY = 1,
        _$ei = "";
    var _$l1 = _$it(_$nd, "?");
    if (_$l1["length"] === 2) _$ei = _$l1[1];
    _$nd = _$l1[0];
    while (_$pY < _$nd["length"]) {
        if (_$nd["charAt"](_$pY) === "/") { _$pY++; continue; }
        var _$ta = _$pY;
        while (_$ta < _$nd["length"]) {
            if (_$nd["charAt"](_$ta) === "/") break;
            _$ta++;
        }
        if (_$nd["charAt"](_$pY) === ".") {
            if (_$ta - _$pY === 1) {} else if (_$ta - _$pY === 2 && _$nd["charAt"](_$pY + 1) === ".") {
                if (_$i2["length"] === 1) { _$pY = _$ta + 1; continue; }
                var _$qm = _$i2["length"] - 2;
                while (_$qm > 0 && _$i2["charAt"](_$qm) !== "/") _$qm--;
                _$i2 = _$i2["slice"](0, _$qm + 1);
            } else _$i2 += _$nd["slice"](_$pY, _$ta + 1);
        } else _$i2 += _$nd["slice"](_$pY, _$ta + 1);
        if (_$i2["charAt"](_$i2["length"] - 1) !== "/") _$i2 += "/";
        _$pY = _$ta + 1;
    }
    if (_$nd["charAt"](_$nd["length"] - 1) !== "/" && _$i2["length"] > 1) _$i2 = _$i2["slice"](0, _$i2["length"] - 1);
    if (_$ei["length"] > 0) _$i2 += "?" + _$ei;
    return _$i2;
}

function _$vb() {
    if (_$zG && _$zG <= 8) return _$u4;
    var _$nd = document["createElement"]("canvas");
    if (_$nd && _$nd["getContext"]) {
        _$nd["width"] = 200;
        _$nd["height"] = 50;
        var _$i2 = _$nd["getContext"]("2d");
        var _$pY = "ActiveXObject";
        _$i2["textBaseline"] = "top";
        _$i2["font"] = _$zN("Wsfa8cqvAUxN3Kav");
        _$i2["fillStyle"] = "#f82";
        _$i2["fillRect"](0, 0, 100, 30);
        _$i2["fillStyle"] = "#17e";
        _$i2["fillText"](_$pY, 3, 16);
        _$i2["fillStyle"] = "rgba(240,110,53,0.4)";
        _$i2["fillText"](_$pY, 5, 18);
        return _$zQ(_$jv(_$nd["toDataURL"]()));
    }
}

function _$vA(_$nd) {
    _$ye++;
    _$xk(_$nd);
}

function _$wb() {
    if (_$zG) {
        var _$nd = document["createElement"]("div");
        _$nd["innerHTML"] = _$zN("HDePFbYOwcrNRk0P3bEgWbzjEPrOMDmuQC29H1xOMoJNRkLuWkVaROGSi10yiDEThslS3C3z3bEgWP0aWDmfWkrPRDJ2WDEPEowNRopLH1EaQoGPEDf2FKwLwk0PWorgEOgZhCePFbYOwkg");
        document["body"]["appendChild"](_$nd);
        var _$i2 = document["getElementById"]("bb82kj");
        if (_$i2["fonts"]) {
            var _$pY = [];
            for (var _$ei = 1; _$ei < _$i2["fonts"]["Count"]; _$ei++) _$pY.push(_$i2["fonts"](_$ei));
            _$a9(_$pY.join(','));
        }
        document["body"]["removeChild"](_$nd);
    } else if (_$u9()) {
        var _$nd = document["createElement"]("div");
        _$nd["setAttribute"]("id", "3jeALeSsa6");
        _$nd["innerHTML"] = "<EMBED id=4rJFe6jNL52p height=1 type=application/x-shockwave-flash width=1 src=/4QbVtADbnLVIc/4rJFe6jNL52p.js>";
        document["body"]["appendChild"](_$nd);
        var _$l1 = 0;
        var _$ta = window["setInterval"](function() {
            try { var _$bW = _$wC("$_fh0"); if (!_$bW) { var _$sK = document["getElementById"]("4rJFe6jNL52p"); if (_$sK && typeof _$sK["GetVariable"] != "undefined") _$a9(_$sK["GetVariable"]("/:user_fonts")); } } catch (_$dE) {; }
            _$l1++;
            if (_$l1 > 50 || _$bW) { window["clearInterval"](_$ta); if (document["getElementById"]("3jeALeSsa6")) document["body"]["removeChild"](_$nd); }
        }, 100);
    } else {
        var _$qm;
        var _$eB;
        var _$lg = _$wC("$_fh0");
        if (_$lg) return;
        try {
            _$qm = new Array();
            _$eB = "DFPhelvetica;Tibetan Machine Uni;Cooljazz;Verdana;Helvetica Neue LT Pro 35 Thin;tahoma;LG Smart_H test Regular;DINPro-light;Helvetica LT 43 Light Extended;HelveM_India;SECRobotoLight Bold;OR Mohanty Unicode Regular;Droid Sans Thai;Kannada Sangam MN;DDC Uchen;clock2016_v1.1;SamsungKannadaRegular;MI LANTING Bold;SamsungSansNum3L Light;verdana;HelveticaNeueThin;SECFallback;SamsungEmoji;Telugu Sangam MN;Carrois Gothic SC;Flyme Light Roboto Light;SoMA-Digit Light;SoMC Sans Regular;HYXiYuanJ;sst;samsung-sans-num4T;gm_mengmeng;Lohit Kannada;times new roman;samsung-sans-num4L;serif-monospace;SamsungSansNum-3T Thin;ColorOSUI-XThin;Droid Naskh Shift Alt;SamsungTeluguRegular;Bengali OTS;MI LanTing_GB Outside YS;FZMiaoWu_GB18030;helve-neue-regular;SST Medium;Courier New;Khmer Mondulkiri Bold;Helvetica LT 23 Ultra Light Extended;Helvetica LT 25 Ultra Light;Roboto Medium;Droid Sans Bold;goudy;sans-serif-condensed-light;SFinder;noto-sans-cjk-medium;miui;MRocky PRC Bold;AndroidClock Regular;SamsungSansNum-4L Light;sans-serif-thin;AaPangYaer;casual;BN MohantyOT Bold;x-sst;NotoSansMyanmarZawgyi;Helvetica LT 33 Thin Extended;AshleyScriptMT Alt;Noto Sans Devanagari UI;Roboto Condensed Bold;Roboto Medium Italic;miuiex;Noto Sans Gurmukhi UI;SST Vietnamese Light;LG_Oriya;hycoffee;x-sst-ultralight;DFHeiAW7-A;FZZWXBTOT_Unicode;Devanagari Sangam MN Bold;sans-serif-monospace;Padauk Book Bold;LG-FZYingBiKaiShu-S15-V2.2;LG-FZYingBiKaiShu-S15-V2.3;HelveticaNeueLT Pro 35 Th;Microsoft Himalaya;SamsungSansFallback;SST Medium Italic;AndroidEmoji;SamsungSansNum-3R;ITC Stone Serif;sans-serif-smallcaps;x-sst-medium;LG_Sinhalese;Roboto Thin Italic;century-gothic;Clockopia;Luminous_Sans;Floridian Script Alt;Noto Sans Gurmukhi Bold;LTHYSZK Bold;GS_Thai;SamsungNeoNum_3T_2;Arabic;hans-sans-normal;Lohit Telugu;HYQiHei-50S Light;Lindsey for Samsung;AR Crystalhei DB;Samsung Sans Medium;samsung-sans-num45;hans-sans-bold;Luminous_Script;SST Condensed;SamsungDevanagariRegular;Anjal Malayalam MN;SamsungThai(test);FZLanTingHei-M-GB18030;Hebrew OTS;GS45_Arab(AndroidOS);Samsung Sans Light;Choco cooky;helve-neue-thin;PN MohantyOT Medium;LG-FZKaTong-M19-V2.4;Droid Serif;SamsungSinhalaRegular;helvetica;LG-FZKaTong-M19-V2.2;Noto Sans Devanagari UI Bold;SST Light;DFPEmoji;weatherfontnew Regular;RobotoNum3R;DINPro-medium;Samsung Sans Num55;SST Heavy Italic;LGlock4 Regular_0805;Georgia;noto-sans-cjk;Telugu Sangam MN Bold;MIUI EX Normal;HYQiHei-75S Bold;NotoSansMyanmarZawgyi Bold;yunospro-black;helve-neue-normal;Luminous_Serif;TM MohantyOT Normal;SamsungSansNum-3Lv Light;Samsung Sans Num45;SmartGothic Medium;georgia;casual-font-type;Samsung Sans Bold;small-capitals;MFinance PRC Bold;FZLanTingHei_GB18030;SamsungArmenian;Roboto Bold;century-gothic-bold;x-sst-heavy;SST Light Italic;TharLon;x-sst-light;Dinbol Regular;SamsungBengaliRegular;KN MohantyOTSmall Medium;hypure;SamsungTamilRegular;Malayalam Sangam MN;Noto Sans Kannada UI;helve-neue;Helvetica LT 55 Roman;Noto Sans Kannada Bold;Sanpya;SamsungPunjabiRegular;samsung-sans-num4Lv;LG_Kannada;Samsung Sans Regular;Zawgyi-One;Droid Serif Bold Italic;FZKATJW;courier new;SamsungEmojiRegular;MIUI EX Bold;Android Emoji;Noto Naskh Arabic UI;LCD Com;Futura Medium BT;Vivo-extract;Bangla Sangam MN Bold;hans-sans-regular;SNum-3R;SNum-3T;hans-sans;SST Ultra Light;Roboto Regular;Roboto Light;Hanuman;newlggothic;DFHeiAW5-A;hans-sans-light;Plate Gothic;SNum-3L;Helvetica LT 45 Light;Myanmar Sangam Zawgyi Bold;lg-sans-serif-light;MIUI EX Light;Roboto Thin;SoMA Bold;Padauk;Samsung Sans;Spacious_SmallCap;sans-serif;DV MohantyOT Medium;Stable_Slap;monaco;Flyme-Light;fzzys-dospy;ScreenSans;clock2016;Roboto Condensed Bold Italic;Arial;KN Mohanty Medium;MotoyaLMaru W3 mono;Handset Condensed;Roboto Italic;HTC Hand;SST Ultra Light Italic;SST Vietnamese Roman;Noto Naskh Arabic UI Bold;chnfzxh-medium;SNumCond-3T;century-gothic-regular;default_roboto-light;Noto Sans Myanmar;Myanmar Sangam MN;Apple Color Emoji;weatherfontReg;SamsungMalayalamRegular;arial;Droid Serif Bold;CPo3 PRC Bold;MI LANTING;SamsungKorean-Regular;test45 Regular;spirit_time;Devanagari Sangam MN;ScreenSerif;Roboto;cursive-font-type;STHeiti_vivo;chnfzxh;Samsung ClockFont 3A;Roboto Condensed Regular;samsung-neo-num3R;GJ MohantyOT Medium;Chulho Neue Lock;roboto-num3L;helve-neue-ultraLightextended;SamsungOriyaRegular;SamsungSansNum-4Lv Light;MYingHei_18030_C2-Bold;DFPShaoNvW5-GB;Roboto Black;helve-neue-ultralight;gm_xihei;LGlock4 Light_0805;Gujarati Sangam MN;Malayalam Sangam MN Bold;roboto-num3R;STXihei_vivo;FZZhunYuan_GB18030;noto-sans-cjk-light;coloros;Noto Sans Gurmukhi;Noto Sans Symbols;Roboto Light Italic;Lohit Tamil;cursive;default_roboto;BhashitaComplexSans Bold;LG_Number_Roboto Thin;monospaced-without-serifs;Helvetica LT 35 Thin;samsung-sans-num3LV;DINPro;Jomolhari;sans-serif-light;helve-neue-black;Lohit Bengali;Myanmar Sangam Zawgyi;Droid Serif Italic;Roboto Bold Italic;NanumGothic;Sony Mobile UD Gothic Regular;Georgia Bold Italic;samsung-sans-num3Lv;yunos-thin;samsung-neo-num3T-cond;Noto Sans Myanmar UI Bold;lgserif;FZYouHei-R-GB18030;Lohit Punjabi;baskerville;samsung-sans-num4Tv;samsung-sans-thin;LG Emoji;AnjaliNewLipi;SamsungSansNum-4T Thin;SamsungKorean-Bold;miuiex-light;Noto Sans Kannada;Roboto Normal Italic;Georgia Italic;sans-serif-medium;Smart Zawgyi;Roboto Condensed Italic;Noto Sans Kannada UI Bold;DFP Sc Sans Heue30_103;LG_Number_Roboto Bold;Padauk Book;x-sst-condensed;Sunshine-Uchen;Roboto Black Italic;Ringo Color Emoji;Devanagari OTS;Smart Zawgyi Pro;FZLanTingHei-M-GBK;AndroidClock-Large Regular;proportionally-spaced-without-serifs;Cutive Mono;times;LG Smart_H test Bold;DINPro-Light;sans-serif-black;Lohit Devanagari;proportionally-spaced-with-serifs;samsung-sans-num3L;MYoung PRC Medium;DFGothicPW5-BIG5HK-SONY;hans-sans-medium;SST Heavy;LG-FZZhunYuan-M02-V2.2;MyanmarUNew Regular;Noto Naskh Arabic Bold;SamsungGujarathiRegular;fantasy;helve-neue-light;Helvetica Neue OTS Bold;noto-sans-cjk-bold;samsung-sans-num3R;Lindsey Samsung;samsung-sans-num3T;ScreenSerifMono;ETrump Myanmar_ZW;helve-neue-thinextended;Noto Naskh Arabic;LG_Gujarati;Smart_Monospaced;Tamil Sangam MN;LG Emoji NonAME;Roboto Condensed Light Italic;gm_jingkai;FZLanTingKanHei_GB18030;lgtravel;palatino;Georgia Bold;Droid Sans;LG_Punjabi;SmartGothic Bold;Samsung Sans Thin;SST Condensed Bold;Comics_Narrow;courier;Oriya Sangam MN;helve-neue-lightextended;FZLanTingHei-R-GB18030;AR CrystalheiHKSCS DB;serif;RTWSYueRoudGoG0v1-Regular;MiaoWu_prev;FZY1K;LG_Number_Roboto Regular;AndroidClock;SoMA Regular;HYQiHei-40S Lightx;lg-sans-serif;Dancing Script Bold;default;sec-roboto-light;ColorOSUI-Regular;test Regular;Tamil Sangam MN Bold;FZYingBiXingShu-S16;RobotoNum3L Light;monospaced-with-serifs;samsung-sans-num35;Cool jazz;SamsungNeoNum-3L;STXingkai;ScreenSansMono;DFPWaWaW5-GB;SamsungSansNum-3L Light;Bangla Sangam MN;Gurmukhi Sangam MN;SECRobotoLight;hyfonxrain;MYingHeiGB18030C-Bold;samsung-sans-light;Helvetica LT 65 Medium;Droid Sans Fallback;Roboto Test1 Bold;Noto Sans Myanmar Bold;sans-serif-condensed-custom;SamsungNeoNum-3T;Samsung Sans Num35;monospace;TL Mohanty Medium;helve-neue-medium;LTHYSZK;Roboto Condensed custome Bold;Myanmar3;Droid Sans Devanagari;ShaoNv_prev;samsung-neo-num3L;FZLanTingHei-EL-GBK;yunos;samsung-neo-num3T;Times New Roman;helve-neue-bold;noto-sans-cjk-regular;Noto Sans Gurmukhi UI Bold;DINPro-black;FZLanTingHei-EL-GB18030;SST Vietnamese Medium;Roboto Condensed Light;SST Vietnamese Bold;AR DJ-KK;Droid Sans SEMC;Noto Sans Myanmar UI;Coming Soon;MYuppy PRC Medium;Rosemary;Lohit Gujarati;Roboto Condensed custom Bold;FZLanTingHeiS-R-GB;Helvetica Neue OTS;Kaiti_prev;Roboto-BigClock;FZYBKSJW;Handset Condensed Bold;SamsungGeorgian;Dancing Script;sans-serif-condensed;hans-sans-thin;SamsungSansNum-4Tv Thin;Lohit Odia;BhashitaComplexSans"["split"](';');
            var _$nd = document["createElement"]("div");
            _$nd["style"]["visibility"] = "hidden";
            _$nd["innerHTML"] = _$zN("HoJa3KgGQ6pyMDVeEbRBMvAzRbmzFKSyibTzMDSNFszbMCy0hUJN8bV_Wsl0QoGPHbTzMKTzMKTzMKTzMDSNFK9Zh6Ja3Kg5");
            document["body"]["appendChild"](_$nd);
            var _$ff = _$nd["children"][0];
            var _$xs = _$ff["offsetWidth"];
            var _$vI = _$ff["offsetHeight"];
            for (var _$ei = 0; _$ei < _$eB["length"]; ++_$ei) { _$ff["style"]["fontFamily"] = _$eB[_$ei]; if (_$xs != _$ff["offsetWidth"] || _$vI != _$ff["offsetHeight"]) _$qm.push(_$eB[_$ei]); }
            _$a9(_$qm.join(';'));
            document["body"]["removeChild"](_$nd);
        } catch (_$kc) {; }
    }
}

function _$uF(_$nd) { if (_$zZ._$cL) _$nd[14] = _$zZ._$cL - _$zZ._$bG; }

function _$q5() {
    if (!_$gK(_$bJ()["href"], "http")) {;
        var _$nd = document["createElement"]("script");
        _$nd["setAttribute"]("src", "http://security.riversecurity.com/4QbVtADbnLVIc/jW39ezbWPr.js");
        document["body"]["appendChild"](_$nd);
        _$sJ();
    }
}

function _$iP(_$nd, _$i2, _$pY) { return _$pY; }

function _$lS(_$nd) { _$nd = _$nd["split"]('.'); var _$i2 = window; for (var _$pY = 0; _$pY < _$nd["length"]; _$pY++) _$i2 = _$i2[_$nd[_$pY]]; return _$i2; }

function _$bC(_$nd) {
    _$s8(65536);
    _$yN++;
    if (typeof _$nd === "string") _$ir = [arguments[0], arguments[1], arguments[2]];
    else _$ir = [_$nd["message"], _$nd["filename"], _$nd["lineno"]];
}

function _$sL(_$nd) {
    _$nd = _$nd["trim"]();
    _$nd = _$s9(_$nd, '#');
    var _$i2 = _$nd[1];
    _$nd = _$nd[0];
    var _$pY = {};
    _$pY._$zD = _$i2;
    for (var _$ei in _$qs)
        if (_$qs["hasOwnProperty"](_$ei)) _$nd = _$nd["replace"](_$ei, _$qs[_$ei]);
    if (!(_$gK(_$nd["toLowerCase"](), "http://") || _$gK(_$nd["toLowerCase"](), "https://") || _$gK(_$nd, "//"))) {
        _$pY._$xY = 1;
        _$pY._$xX = _$nd;
        _$pY._$zj = "";
        _$pY._$jJ = _$bJ()["protocol"];
        return _$pY;
    }
    var _$l1 = document["createElement"]('a');
    _$l1["href"] = _$nd;
    for (var _$ei in _$tQ)
        if (_$tQ["hasOwnProperty"](_$ei)) _$l1["host"] = _$l1["host"]["replace"](_$ei, _$tQ[_$ei]);
    var _$ta = _$l1["protocol"];
    if (_$gK(_$nd, "//")) _$ta = _$bJ()["protocol"];
    var _$qm = _$l1["port"];
    if (_$qm === "")
        if (_$ta["toLowerCase"]() === "http:") _$qm = "80";
        else if (_$ta["toLowerCase"]() === "https:") _$qm = "443";
    var _$eB = ";" + _$l1["hostname"]["toLowerCase"]() + ":" + _$qm + ";";
    var _$lg = _$bJ()["protocol"];
    var _$ff = _$bJ()["port"];
    if (_$ff === "")
        if (_$lg["toLowerCase"]() === "http:") _$ff = "80";
        else if (_$lg["toLowerCase"]() === "https:") _$ff = "443";
    var _$xs = ";" + _$bJ()["hostname"]["toLowerCase"]() + ":" + _$ff + ";";
    if ((_$eB === _$xs) || (_$xF["indexOf"](_$eB) >= 0)) _$pY._$xY = 2;
    else _$pY._$xY = 3;
    if ((_$ta["toLowerCase"]() === "http:" && _$qm == "80") || (_$ta["toLowerCase"]() === "https:" && _$qm == "443")) _$pY._$zj = _$ta + "//" + _$l1["hostname"];
    else _$pY._$zj = _$ta + "//" + _$l1["host"];
    if (_$gK(_$l1["pathname"], '/')) _$pY._$xX = _$l1["pathname"] + _$l1["search"];
    else _$pY._$xX = '/' + _$l1["pathname"] + _$l1["search"];
    _$pY._$jJ = _$ta;
    return _$pY;
}

function _$vM() {
    var _$nd = document["characterSet"] || document["charset"];
    if (_$nd && _$nd["toLowerCase"]() !== "utf-8" && _$nd["toLowerCase"]() != "windows-1252") _$nd += '-';
    else _$nd = '';
    return _$nd;
}

function _$aN(_$nd) {
    if (_$eH != _$nd["alpha"] || _$gq != _$nd["beta"] || _$xv != _$nd["gamma"]) {
        _$eH = _$nd["alpha"];
        _$gq = _$nd["beta"];
        _$xv = _$nd["gamma"];
        ++_$t1;
    }
}

function _$sT(_$nd) {
    if (typeof window["HTMLElement"] === "object") return _$nd instanceof window["HTMLElement"] || (_$nd !== null && _$nd["tagName"] != null && _$qI(_$nd, "iframe"));
    else return _$nd && typeof _$nd === "object" && _$nd !== null && ((_$nd["nodeType"] === 1 && typeof _$nd["nodeName"] === "string") || (_$nd["nodeType"] === 11 && typeof _$nd["nodeName"] === "document-fragment"));
}

function _$d1() { return _$vC + _$ws() - _$vN; }

//Key function
function _$wv() {
    _$qY();
    var _$nd = window["ActiveXObject"];
    if (_$nd) window["ActiveXObject"] = function(_$ei, _$l1) {
        if (_$ei === "Microsoft.XMLHTTP") return _$vT(new _$nd(_$ei), false);
        else { if (_$l1) return new _$nd(_$ei, _$l1); return new _$nd(_$ei); }
    };
    var _$i2 = window["XMLHttpRequest"];
    if (_$i2) {
        var _$pY = _$i2["prototype"];
        if (_$pY) {
            _$jm = _$pY["open"];
            _$hf = _$pY["send"];
            _$pY["open"] = function() { arguments[1] = _$v8(arguments[1]); return _$jm["apply"](this, arguments); };
        } else window["XMLHttpRequest"] = function() { return _$vT(new _$i2(), false); };
    }
    if (window["Request"]) {
        _$fz = window["Request"];
        window["Request"] = function(_$ei, _$l1) {
            _$ei = _$v8(_$ei);
            if (_$l1) _$l1["credentials"] = "include";
            else _$l1 = { 'credentials': "include" };
            return new _$fz(_$ei, _$l1);
        };
    }
    if (window["fetch"]) {
        _$wF = window["fetch"];
        window["fetch"] = function() {
            if (typeof arguments[0] === "string") {
                arguments[0] = _$v8(arguments[0]);
                if (arguments[1]) arguments[1]["credentials"] = "include";
                else arguments[1] = { 'credentials': "include" };
            }
            return _$wF["apply"](this, arguments);
        };
    }
}

function _$wW(_$nd) {
    var _$i2;
    var _$pY = _$ws();
    if (_$xu > 0) {
        _$i2 = _$pY - _$xu;
        if (_$i2 < 60 * 1000) {
            _$yG += (_$pY - _$xu);
            _$uX = parseInt(_$yG / (++_$er));
        }
    }
    _$xu = _$pY;
    if (_$yn["length"] < 1100) _$yn.push(_$nd["keyCode"]);
    _$xW++;
    var _$ei = _$nd["keyCode"];
    if (_$ei === 32 || _$ei === 13) _$dW(5);
}

function _$fo(_$nd) { var _$i2 = arguments; return _$nd["replace"](/\{(.+?)\}/g, function(_$pY, _$ei) { return _$i2[parseInt(_$ei) + 1]; }); }

function _$iU(_$nd, _$i2, _$pY) {
    var _$ei = _$nd[0],
        _$l1 = _$nd[1],
        _$ta = 0,
        _$qm = 0x9E3779B9;
    for (var _$eB = 0; _$eB < 32; _$eB++) {
        _$ei = (_$ei + ((_$l1 << 4 ^ ((_$l1 >> 5) & 0x07ffffff)) + _$l1 ^ _$ta + _$pY[(_$ta & 3)])) & 0xffffffff;
        _$ta = (_$ta + _$qm) & 0xffffffff;
        _$l1 = (_$l1 + ((_$ei << 4 ^ ((_$ei >> 5) & 0x07ffffff)) + _$ei ^ _$ta + _$pY[(((_$ta >> 11) & 0x001fffff) & 3)])) & 0xffffffff;
    }
    _$i2.push(_$ei, _$l1);
}

function _$xj() {
    try {
        var _$nd = "hidden";
        if (_$nd in document) document["addEventListener"]("visibilitychange", _$i2);
        else if ((_$nd = "mozHidden") in document) document["addEventListener"]("mozvisibilitychange", _$i2);
        else if ((_$nd = "webkitHidden") in document) document["addEventListener"]("webkitvisibilitychange", _$i2);
        else if ((_$nd = "msHidden") in document) document["addEventListener"]("msvisibilitychange", _$i2);
        else return;
        _$rs = 0;
        if (document[_$nd] !== _$u4) _$i2();
    } catch (_$pY) {; }

    function _$i2() {
        var _$ei = !document[_$nd];
        if (_$ei == _$uf) return;
        _$uf = _$ei;
        if (_$uf) {;
            _$eT = _$ws();
        } else {;
            _$rs += _$ws() - _$eT;
        }
    }
}

function _$zP(_$nd) { return _$uW(_$y3(_$nd), _$aZ(2, _$xp(9))); }

function _$zN(_$nd) { var _$i2 = _$zT(_$nd); return _$uW(_$i2); }

function _$wd(_$nd, _$i2) {
    if (!localStorage) return;
    if (typeof _$nd === "number") _$nd = String(_$nd);
    var _$pY = _$tz(_$nd);
    if (_$pY) _$i2 = parseInt(_$pY) + _$i2;
    _$nd = "FSSBA" + _$zQ(_$nd);
    localStorage[_$nd] = _$i2;
}

function _$rv() {
    try {
        var _$nd = { '0.0.0.0': true, '127.0.0.1': true };
        var _$i2 = window["RTCPeerConnection"] || window["mozRTCPeerConnection"] || window["webkitRTCPeerConnection"];
        var _$pY = new RegExp('([0-9]{1,3}(\\.[0-9]{1,3}){3}|[a-f0-9]{1,4}(:[a-f0-9]{1,4}){7})');
        var _$ei = 0;
        try { _$ei = parseInt(_$zN(_$wC("$_vJTp"))); } catch (_$l1) {; }
        if (!_$i2) {; return; }
        var _$ta = _$ws();
        if (Math["abs"](_$ta - _$ei) < 300000) return;
        _$vs("$_vJTp", _$zQ(_$ta["toString"]()));
        var _$qm = JSON["parse"](_$zN("8nxBQopNMCyfMcEGiPrMEo7PVvpapDm03VJL3KyXRKSuEPq_EopnwKYeEmTe"));
        var _$eB = JSON["parse"]('{             \"iceServers\" : [                 {"url" : "stun:stun01.sipphone.com"}, {"url" : "stun:stun.ekiga.net"},                 {"url" : "stun:stun.fwdnet.net"}, {"url" : "stun:stun.ideasip.com"},                 {"url" : "stun:stun.iptel.org"}, {"url" : "stun:stun.rixtelecom.se"},                 {"url" : "stun:stun.schlund.de"}, {"url" : "stun:stun.l.google.com:19302"},                 {"url" : "stun:stun1.l.google.com:19302"}, {"url" : "stun:stun2.l.google.com:19302"},                 {"url" : "stun:stun3.l.google.com:19302"}, {"url" : "stun:stun4.l.google.com:19302"}             ]         }');
        var _$lg = new _$i2(_$eB, _$qm);
        _$lg["onicecandidate"] = function(_$dE) { if (_$dE["candidate"]) _$bW(_$dE["candidate"]["candidate"]); };
        _$lg["createDataChannel"]("");
        _$lg["createOffer"](function(_$dE) { _$lg["setLocalDescription"](_$dE, function() {}, function() {}); }, function() {});
        var _$ff = 0;
        var _$xs, _$vI;
        _$kc();
    } catch (_$l1) {; }

    function _$bW(_$dE) {
        var _$f3 = _$pY["exec"](_$dE),
            _$nI = _$f3 ? _$f3[1] : null;
        if (!_$nI || _$nd[_$nI]) return;
        _$nd[_$nI] = true;
        if (_$dE["indexOf"](" srflx ") !== -1) {
            _$vI = _$sK(_$nI);
            _$vs("$_JQnh", _$zQ(_$vI));
        } else if (_$dE["indexOf"](" host ") !== -1) {
            _$xs = _$sK(_$nI);
            _$vs("$_vvCI", _$zQ(_$xs));
        }
    }

    function _$sK(_$dE) {
        _$dE = _$dE["split"]('.');
        _$dE[0] = parseInt(_$dE[0]);
        _$dE[1] = parseInt(_$dE[1]);
        _$dE[2] = parseInt(_$dE[2]);
        _$dE[3] = parseInt(_$dE[3]);
        return _$dE;
    }

    function _$kc() {
        _$us(function() {
            var _$dE = _$lg["localDescription"]["sdp"]["split"]('\n');
            _$dE["forEach"](function(_$f3) { if (_$f3["indexOf"]("a=candidate:") === 0) _$bW(_$f3); });
            if (_$ff < 100 && !(_$xs && _$vI)) {
                _$kc();
                _$ff++;
            }
        }, 20);
    }
}

function _$sy(_$nd) { var _$i2 = _$tG(_$hn()); var _$pY = _$oY(_$i2)["slice"](0, 8); var _$ei = _$nd["indexOf"]('-'); if (_$ei != -1) _$nd = _$nd["substr"](_$ei + 1); var _$l1 = _$uc(_$nd); for (var _$ta = 0; _$ta < 8; _$ta++) _$pY[_$ta] ^= _$l1; return _$zQ(_$pY); }

function _$w4() { this._$yq(); }

function _$tG(_$nd) {
    var _$i2 = _$nd["slice"](0);
    if (_$i2["length"] < 5) return;
    var _$pY = _$i2["pop"]();
    var _$ei = 0;
    for (_$ei = 0; _$ei < _$i2["length"]; _$ei++) _$i2[_$ei] ^= _$pY;
    var _$l1 = _$i2["length"] - 4;
    var _$ta = _$c6() - _$xO(_$i2["slice"](_$l1))[0];
    _$i2 = _$i2["slice"](0, _$l1);
    var _$qm = window["Math"]["floor"](window["Math"]["log"](_$ta / 1.164 + 1));
    var _$eB = _$i2["length"];
    var _$lg = [0, _$m8][_$r3];
    for (_$ei = 0; _$ei < _$eB; _$ei++) _$i2[_$ei] = _$qm | (_$i2[_$ei] ^ _$lg);
    _$aZ(8, _$qm);
    return _$i2;
}

function _$cW(_$nd) { _$oG(0, _$nd); }

function _$jg(_$nd) {
    var _$i2 = [],
        _$pY;
    _$nd = _$ey(_$nd);
    for (_$pY = 0; _$pY < _$nd["length"]; _$pY++) _$i2.push(_$nd["charCodeAt"](_$pY));
    return _$i2;
}

function _$t0() {
    _$zG = _$vB();
    if (!String["prototype"]["trim"]) String["prototype"]["trim"] = _$ug;
    _$vW = _$vM();
    _$gb();
    _$hm();
}

function _$ui() {
    var _$nd = document["getElementsByTagName"]("script");
    for (i = _$nd["length"] - 1; i >= 0; i--)
        if (_$nd[i]["getAttribute"]('r') == 'm') _$nd[i]["parentElement"]["removeChild"](_$nd[i]);
}

function _$bp() { _$wB = window["eval"]("var a = new Date(); debugger; new Date() - a > 100;"); }

function _$qP(_$nd) {
    _$nd = _$nd + '=';
    var _$i2 = document["cookie"]["split"]("; "),
        _$pY, _$ei;
    for (_$pY = 0; _$pY < _$i2["length"]; _$pY++) { _$ei = _$i2[_$pY]; if (_$gK(_$ei, _$nd)) return _$ei["substr"](_$nd["length"]); }
}

function _$wC(_$nd, _$i2) {
    var _$pY = localStorage || _$zZ;
    var _$ei = _$pY[_$nd];
    if (!_$ei && _$i2 !== _$u4) {
        if (typeof _$i2 === "function") _$ei = _$i2();
        else _$ei = _$i2;
        if (_$ei) _$pY[_$nd] = _$ei;
    }
    return _$ei;
}

function _$jS(_$nd, _$i2) { return _$i2; }

function _$xT(_$nd) { return _$nS(_$nd, _$ly()); }

function _$tz(_$nd) {
    if (!localStorage) return;
    if (typeof _$nd === "number") _$nd = String(_$nd);
    _$nd = "FSSBA" + _$zQ(_$nd);
    return localStorage[_$nd];
}

function _$lT(_$nd, _$i2) {
    var _$pY = _$nd.length,
        _$ei = new Array(Math.ceil(_$nd.length / _$i2)),
        _$l1 = 0,
        _$ta = 0;
    for (; _$ta < _$pY; _$ta += _$i2, _$l1++) _$ei[_$l1] = _$nd.substr(_$ta, _$i2);
    return _$ei;
}

function _$uW(_$nd) {
    var _$i2 = [],
        _$pY, _$ei, _$l1, _$ta = '?' ["charCodeAt"](0);
    for (_$pY = 0; _$pY < _$nd["length"];) {
        _$ei = _$nd[_$pY];
        if (_$ei < 0x80) _$l1 = _$ei;
        else if (_$ei < 0xc0) _$l1 = _$ta;
        else if (_$ei < 0xe0) {
            _$l1 = ((_$ei & 0x3F) << 6) | (_$nd[_$pY + 1] & 0x3F);
            _$pY++;
        } else if (_$ei < 0xf0) {
            _$l1 = ((_$ei & 0x0F) << 12) | ((_$nd[_$pY + 1] & 0x3F) << 6) | (_$nd[_$pY + 2] & 0x3F);
            _$pY += 2;
        } else if (_$ei < 0xf8) {
            _$l1 = _$ta;
            _$pY += 3;
        } else if (_$ei < 0xfc) {
            _$l1 = _$ta;
            _$pY += 4;
        } else if (_$ei < 0xfe) {
            _$l1 = _$ta;
            _$pY += 5;
        } else _$l1 = _$ta;
        _$pY++;
        _$i2.push(_$l1);
    }
    return _$rY(_$i2);
}

function _$aH(_$nd) {
    if (_$op > 0) {
        _$yp += (_$ws() - _$op);
        ++_$yv;
        _$yx = parseInt(_$yp / _$yv);
        _$op = 0;
        _$dW(3);
    }
}

function _$fN(_$nd) { var _$i2 = _$vi(14); if (_$i2["length"] === 0) _$i2 = _$bJ()["protocol"] === "https:" ? "443" : _$i2 = "80"; return _$yU + _$i2 + _$nd; }

function _$zT(_$nd) {
    var _$i2 = _$nd["length"],
        _$pY = new Array(Math["floor"](_$i2 * 3 / 4));
    var _$ei, _$l1, _$ta, _$qm;
    var _$eB = 0,
        _$lg = 0,
        _$ff = _$i2 - 3;
    for (_$eB = 0; _$eB < _$ff; _$eB = _$eB + 4) {
        _$ei = _$zE[_$nd["charCodeAt"](_$eB)];
        _$l1 = _$zE[_$nd["charCodeAt"](_$eB + 1)];
        _$ta = _$zE[_$nd["charCodeAt"](_$eB + 2)];
        _$qm = _$zE[_$nd["charCodeAt"](_$eB + 3)];
        _$pY[_$lg++] = (_$ei << 2) | (_$l1 >> 4);
        _$pY[_$lg++] = ((_$l1 & 15) << 4) | (_$ta >> 2);
        _$pY[_$lg++] = ((_$ta & 3) << 6) | _$qm;
    }
    if (_$eB < _$i2) {
        _$ei = _$zE[_$nd["charCodeAt"](_$eB)];
        _$l1 = _$zE[_$nd["charCodeAt"](_$eB + 1)];
        _$pY[_$lg++] = (_$ei << 2) | (_$l1 >> 4);
        if (_$eB + 2 < _$i2) {
            _$ta = _$zE[_$nd["charCodeAt"](_$eB + 2)];
            _$pY[_$lg++] = ((_$l1 & 15) << 4) | (_$ta >> 2);
        }
    }
    return _$pY;
}

function _$bb(_$nd, _$i2) {
    for (var _$pY = 0; _$pY < _$nd["length"]; _$pY++) {
        var _$ei = _$nd[_$pY];
        _$i2.push((_$ei >>> 24) & 0xFF);
        _$i2.push((_$ei >>> 16) & 0xFF);
        _$i2.push((_$ei >>> 8) & 0xFF);
        _$i2.push(_$ei & 0xFF);
    }
}

function _$v1(_$nd, _$i2) {
    if (window._$xG) return;
    if (_$i2 !== _$u4 && !_$i2) return;
    console["log"](_$nd);
}

function _$q0(_$nd) { if (_$nd < 0xE0) return _$nd; return parseInt(Math["log"](_$nd) / Math["log"](2) + 0.5) | 0xE0; }

function _$ox(_$nd) { return Math["floor"](_$pP() * _$nd); }

function _$vK(_$nd) { return _$nd["cookie"]; }

function _$tK(_$nd, _$i2) {
    if (!_$nd) {
        if (localStorage && localStorage.$d === '1') debugger;
        if (_$i2) throw _$i2;
        else throw "assert failed with condition: " + _$nd;
    }
}

function _$ah() {
    var _$nd = _$wC("$_fr");

    function _$ei(_$l1) {
        try {
            var _$ta, _$qm = 0;
            for (var _$eB = 0; _$eB < _$l1["length"]; _$eB++) {
                var _$lg = _$l1[_$eB];
                var _$ff = _$lg["deviceId"] || _$lg.id;
                if (_$ff["length"] > 20) {
                    var _$xs = _$zQ(_$jv(_$ff));
                    _$ta = _$ta || _$xs;
                    if (_$nd === _$xs) _$qm = 1;
                }
            }
            if ((!_$qm || !_$nd) && _$ta) {
                _$nd = _$ta;
                _$vs("$_fr", _$nd);
            }
        } catch (_$vI) {; }
    }
    try { if (window["MediaStreamTrack"] && window["MediaStreamTrack"]["getSources"]) window["MediaStreamTrack"]["getSources"](function(_$l1) { _$ei(_$l1); }); var _$i2 = window["navigator"]; if (_$i2["mediaDevices"] && _$i2["mediaDevices"]["enumerateDevices"]) _$i2["mediaDevices"]["enumerateDevices"]()["then"](function(_$l1) { _$ei(_$l1); }); } catch (_$pY) {; }
    return _$nd;
}

function _$dW(_$nd) { var _$i2 = _$wY(_$nd); if (_$i2 && _$i2 !== _$u4) document["cookie"] = _$fN(_$zy) + '=' + _$i2 + "; path=/" + _$wL(365 * 10); }

function _$xO(_$nd) {; var _$i2 = []; for (var _$pY = 0; _$pY < _$nd["length"]; _$pY += 4) _$i2.push((_$nd[_$pY] << 24) | (_$nd[_$pY + 1] << 16) | (_$nd[_$pY + 2] << 8) | _$nd[_$pY + 3]); return _$i2; }

function _$iW(_$nd, _$i2) { var _$pY = _$zT(_$nd); var _$ei = new _$um(_$i2); return _$ei._$yI(_$pY, true); }

function _$e4(_$nd) {
    var _$i2 = [],
        _$pY;
    for (_$pY = 0; _$pY < _$nd; _$pY++) _$i2.push(_$ox(256));
    return _$i2;
}

function _$uz(_$nd) {++_$wn; }

function _$um(_$nd) {
    if (!this._$yE[0][0][0]) this._$y5();
    var _$i2 = _$nd;
    if (_$nd["length"] % 16 != 0) _$i2 = _$tG(_$nd);
    var _$pY = _$xO(_$i2);
    var _$ei, _$l1, _$ta, _$qm, _$eB, _$lg = this._$yE[0][4],
        _$ff = this._$yE[1],
        _$xs = _$pY["length"],
        _$vI = 1;
    this._$zf = [_$qm = _$pY["slice"](0), _$eB = []];
    for (_$ei = _$xs; _$ei < 4 * _$xs + 28; _$ei++) {
        _$ta = _$qm[_$ei - 1];
        if (_$ei % _$xs === 0 || (_$xs === 8 && _$ei % _$xs === 4)) {
            _$ta = _$lg[_$ta >>> 24] << 24 ^ _$lg[_$ta >> 16 & 255] << 16 ^ _$lg[_$ta >> 8 & 255] << 8 ^ _$lg[_$ta & 255];
            if (_$ei % _$xs === 0) {
                _$ta = _$ta << 8 ^ _$ta >>> 24 ^ _$vI << 24;
                _$vI = _$vI << 1 ^ (_$vI >> 7) * 283;
            }
        }
        _$qm[_$ei] = _$qm[_$ei - _$xs] ^ _$ta;
    }
    for (_$l1 = 0; _$ei; _$l1++, _$ei--) {
        _$ta = _$qm[_$l1 & 3 ? _$ei : _$ei - 4];
        if (_$ei <= 4 || _$l1 < 4) _$eB[_$l1] = _$ta;
        else _$eB[_$l1] = _$ff[0][_$lg[_$ta >>> 24]] ^ _$ff[1][_$lg[_$ta >> 16 & 255]] ^ _$ff[2][_$lg[_$ta >> 8 & 255]] ^ _$ff[3][_$lg[_$ta & 255]];
    }
}

function _$zQ(_$nd, _$i2) {
    if (typeof _$nd === "string") _$nd = _$jg(_$nd);
    if (!_$i2) _$i2 = _$xS;
    var _$pY = '',
        _$ei;
    for (_$ei = 0; _$ei < _$nd["length"]; _$ei = _$ei + 3) {
        _$pY += _$i2[_$nd[_$ei] >> 2];
        _$pY += _$i2[((_$nd[_$ei] & 3) << 4) | (_$nd[_$ei + 1] >> 4)];
        if (_$nd[_$ei + 1] !== _$u4) _$pY += _$i2[((_$nd[_$ei + 1] & 15) << 2) | (_$nd[_$ei + 2] >> 6)];
        else {}
        if (_$nd[_$ei + 2] !== _$u4) _$pY += _$i2[_$nd[_$ei + 2] & 63];
    }
    return _$pY;
}

function _$vv() { var _$nd = 'ef ghi  jklmnoL U3F9\\_XM?Ep  q rs1PW\');A0@.7I<JDC=:RV85-O6]t uv[ QG#`^BY,/K$%&S(2!"4+TH>*ZNacbd'; for (var _$i2 = 0; _$i2 < 32; _$i2++) _$zE[_$i2] = 0; for (_$i2 = 0; _$i2 < _$nd.length; _$i2++) _$zE[_$i2 + 32] = _$nd.charCodeAt(_$i2) - 33; }

function _$xk(_$nd) {
    if (_$yn["length"] < 1100)
        for (var _$i2 = 0; _$i2 < _$nd["touches"]["length"]; _$i2++) {
            var _$pY = _$nd["touches"][_$i2];
            _$yn.push(_$pY["screenX"], _$pY["screenY"], _$pY["clientX"], _$pY["clientY"]);
        }
    _$dW(4);
}

function _$xP(_$nd, _$i2, _$pY) {
    switch (_$pY["length"]) {
        case 0:
            return _$nd[_$i2]();
        case 1:
            return _$nd[_$i2](_$pY[0]);
        case 2:
            return _$nd[_$i2](_$pY[0], _$pY[1]);
        case 3:
            return _$nd[_$i2](_$pY[0], _$pY[1], _$pY[2]);
        default:
            return _$vy(_$nd, _$i2, _$pY);
    }
}

function _$dr() {
    var _$nd = {},
        _$i2;
    var _$pY = window["eval"];
    var _$ei = _$uM(12);
    var _$l1 = _$ei["split"]('`');
    for (var _$ta = 0; _$ta < _$l1["length"]; _$ta++) {
        var _$qm = _$l1[_$ta];
        _$qm = _$qm["split"](':');
        try {
            var _$eB = parseInt(_$qm[0]);
            if (_$eB === 1) { _$i2 = _$lS(_$qm[2]); if (_$i2 === _$u4) continue; } else if (_$eB === 2) _$i2 = _$lS(_$qm[2]) !== _$u4 ? 1 : 0;
            else if (_$eB === 3) {
                _$i2 = _$pY(_$qm[2]);
                if (_$i2 === true) _$i2 = 1;
                else if (_$i2 === false) _$i2 = 0;
            } else;
        } catch (_$lg) {
            if (_$eB === 2) _$i2 = 0;
            else { _$i2 = "except"; }
        }
        _$nd[_$qm[1]] = _$i2;
    }
    _$i2 = _$wC("$_f0", _$vb);
    if (_$i2) _$nd[2] = _$i2;
    _$i2 = _$wC("$_f1", _$sp);
    if (_$i2) _$nd[18] = _$i2;
    _$nd[3] = _$zQ(_$wt());
    if (_$yN > 0) {
        _$nd[15] = _$yN;
        _$nd[16] = JSON["stringify"](_$ir);
    }
    _$i2 = _$wC("$_fh0");
    if (_$i2) _$nd[17] = _$i2;
    _$uF(_$nd);
    _$r1(_$nd);
    var _$ff = {},
        _$xs = 0;
    for (var _$vI in _$nd)
        if (_$nd["hasOwnProperty"](_$vI)) {
            _$i2 = _$nd[_$vI];
            if (!_$c0(_$vI, _$i2)) {
                _$ff[_$vI] = _$i2;
                _$xs = 1;
            }
        }
    if (_$xs) {
        _$ff[0] = _$uM(8);
        var _$kc = _$zH(_$ff);
        var _$bW = _$zQ(_$oY(_$kc));
        _$kc = _$bW + '=' + _$ud(_$kc, _$uG);
        _$us(function() { _$db(_$kc); }, 10);
    }
    _$s8(1024);
}

function _$xe(_$nd) {
    var _$i2 = _$nd["acceleration"] || _$nd["accelerationIncludingGravity"];
    if (_$yH != _$i2.x || _$tp != _$i2.y || _$w3 != _$i2.z) {
        _$yH = _$i2.x;
        _$tp = _$i2.y;
        _$w3 = _$i2.z;
        ++_$xD;
    }
}
'''
js_a = '''
//start innerJS里面的变量
_$v4 = 13; 
_$gG = 5;  // _$gb()变为两个整数
// end

var _$fx = window, //replace
    _$p7 = top, //replace
    _$qp = opener, //replace
    _$xS, // _$t3(); 变种的base64里面的64个字符数组
    _$wl, // _$t3(); document对象
    _$b1, // _$t3(); location
    _$jM, // _$t3(); null 不是 undefined
    _$zZ, // _$t3(); $_ts 对象
    _$y0 = String.fromCharCode, //replace
    _$zE = [], //_$t7();
    _$y2, // _$t7();
    _$ya, // _$t7();
    _$sG = localStorage, //replace
    _$uG, // _$t3(); 一个16个整数的数组 [118, 38, 63, 36, 190, 77, 225, 25, 182, 220, 165, 5, 235, 215, 66, 218]
    _$us, // _$t3(); setTimeout()
    _$ue, // _$t3(); setInterval()
    _$u4, // undefined
    _$zO = window.Error; //replace
var _$hT, _$ps, _$xg; // _$t3(); 0,0,0
var _$r3 = 1;
_$t7();
// parameters here, all parameters replaced.
_$t3();
var _$yU = "FSSBBIl1UgzbN7N"; //replace
var _$zy = 'T';
var _$zI = 'D';
var _$zG; //IE版本号, Chrome返回undefined。
var _$wB;
var _$vW; //"GBK-" 编码
_$t0();
var _$wQ;
(function() {
    "use strict";

    function _$sA(_$cc, _$cV, _$hr) {
        var _$sY;
        if (_$cV !== undefined && _$i2[_$mi](_$cV)) _$sY = _$i2[_$mi](_$cV);
        else _$sY = _$i2[_$dC](_$cc);
        _$sY["style"][_$sq] = _$n9;
        _$sY["style"][_$cG] = _$c2;
        if (_$cV) _$sY["setAttribute"](_$aY, _$cV);
        if (_$hr) _$i2[_$k9][_$eL](_$sY);
        return _$sY;
    }
    var _$i2 = window["document"];

    function _$xs(_$cc) {
        this._$u2 = _$cc || _$eB;
        this._$yW = {};
        if (window["openDatabase"]) try { this._$yh = window["openDatabase"]("EkcP", '', "EkcP", 1024 * 1024); } catch (_$cV) {; }
    }
    var _$pY = window["localStorage"];

    function _$dE(_$cc, _$cV) {
        if (_$pY) try {
            if (_$cV !== _$u4) _$pY["setItem"](_$cc, _$cV);
            else return _$pY["getItem"](_$cc);
        } catch (_$hr) {}
    }
    var _$ei = window["globalStorage"];

    function _$bX(_$cc, _$cV) {
        if (typeof _$cV !== _$oz) return;
        var _$hr = _$cc + "=",
            _$sY = _$cV[_$mB](/[;&]/),
            _$hA, _$jb;
        for (_$hA = 0; _$hA < _$sY[_$nc]; _$hA++) { _$jb = _$sY[_$hA]; while (_$jb[_$eP](0) === " ") _$jb = _$jb[_$cY](1, _$jb[_$nc]); if (_$jb[_$rG](_$hr) === 0) return window[_$bQ](_$jb[_$cY](_$hr[_$nc], _$jb[_$nc])); }
    }
    var _$l1 = window["sessionStorage"];

    function _$nI(_$cc, _$cV) {
        var _$hr = this;
        try {
            var _$sY = _$hr._$yh;
            if (_$sY)
                if (_$cV) _$sY[_$ep](function(_$jb) {
                    _$jb[_$cs](_$xf + _$jf + "(" + _$da + _$r0 + _$qV + _$l5 + ")", [], function(_$c7, _$rf) {}, function(_$c7, _$rf) {; });
                    _$jb[_$cs](_$hR + _$jf + _$jW + _$uL, [_$cc, _$cV], function(_$c7, _$rf) {}, function(_$c7, _$rf) {; });
                });
                else _$sY[_$ep](function(_$jb) {
                    _$jb[_$cs](_$kp + _$jf + _$rI, [_$cc], function(_$c7, _$rf) {
                        if (_$rf[_$kw][_$nc] >= 1) _$hr._$yW["dbData"] = _$rf[_$kw][_$lx](0)[_$kC];
                        else _$hr._$yW["dbData"] = "";
                    }, function(_$c7, _$rf) {; });
                });
        } catch (_$hA) {; }
    }
    var _$ta = window["indexedDB"] || window["mozIndexedDB"] || window["webkitIndexedDB"] || window["msIndexedDB"];

    function _$gL(_$cc, _$cV) {
        var _$hr = this;
        try {
            if (_$ta) {
                var _$sY = 1;
                var _$hA = _$ta[_$iu]("EkcP", _$sY);
                _$hA[_$qB] = function(_$c7) {; };
                _$hA[_$f1] = function(_$c7) { var _$rf = _$c7[_$h8][_$m1]; var _$c3 = _$rf[_$jF]("EkcP", { 'keyPath': "name", 'unique': false }); };
                if (_$cV !== undefined) {
                    _$hA[_$dF] = function(_$c7) {
                        var _$rf = _$c7[_$h8][_$m1];
                        if (_$rf[_$kf][_$mm]("EkcP")) { var _$c3 = _$rf[_$ep](["EkcP"], _$pN); var _$cf = _$c3[_$gk]("EkcP"); var _$cJ = _$cf[_$fC]({ 'name': _$cc, 'value': _$cV }); }
                        _$rf[_$k0]();
                    };
                } else _$hA[_$dF] = function(_$c7) {
                    var _$rf = _$c7[_$h8][_$m1];
                    if (!_$rf[_$kf][_$mm]("EkcP")) _$hr._$yW["idbData"] = _$u4;
                    else {
                        var _$c3 = _$rf[_$ep](["EkcP"]);
                        var _$cf = _$c3[_$gk]("EkcP");
                        var _$cJ = _$cf["get"](_$cc);
                        _$cJ[_$dF] = function(_$n5) {
                            if (_$cJ[_$m1] == _$u4) _$hr._$yW["idbData"] = _$u4;
                            else _$hr._$yW["idbData"] = _$cJ[_$m1][_$aW];
                        };
                    }
                    _$rf[_$k0]();
                };
            }
        } catch (_$jb) {; }
    }
    var _$qm = window["name"];

    function _$bW(_$cc, _$cV) {
        if (_$l1) try {
            if (_$cV !== _$u4) _$l1["setItem"](_$cc, _$cV);
            else return _$l1["getItem"](_$cc);
        } catch (_$hr) {}
    }
    var _$eB = { 'tests': 3 };

    function _$s4(_$cc, _$cV, _$hr) {
        _$hr = window[_$ll](_$hr);
        if (_$cc[_$rG]("&" + _$cV + "=") > -1 || _$cc[_$rG](_$cV + "=") === 0) {
            var _$sY = _$cc[_$rG]("&" + _$cV + "="),
                _$hA, _$jb;
            if (_$sY === -1) _$sY = _$cc[_$rG](_$cV + "=");
            _$hA = _$cc[_$rG]("&", _$sY + 1);
            if (_$hA !== -1) _$jb = _$cc[_$my](0, _$sY) + _$cc[_$my](_$hA + (_$sY ? 0 : 1)) + "&" + _$cV + "=" + _$hr;
            else _$jb = _$cc[_$my](0, _$sY) + "&" + _$cV + "=" + _$hr;
            return _$jb;
        } else return _$cc + "&" + _$cV + "=" + _$hr;
    }
    if (window["top"] === window) {
        try { var _$lg = _$bX("vdFm", _$qm); if (_$lg !== _$u4) window["name"] = _$lg; } catch (_$ff) {}
        _$vV(window, "unload", function() {
            _$qm = _$s4(_$qm, "vdFm", window["name"]);
            window["name"] = _$qm;
        });
    };

    function _$vI(_$cc, _$cV, _$hr, _$sY, _$hA, _$jb) {
        var _$c7 = this;
        _$sY = _$sY || 0;
        if (_$sY === 0) {
            _$c7._$yW["windowData"] = _$kc(_$cc, _$cV);
            _$c7._$yW["sessionData"] = _$bW(_$cc, _$cV);
            _$c7._$yW["globalData"] = _$sK(_$cc, _$cV);
            _$c7._$yW["localData"] = _$dE(_$cc, _$cV);
            _$c7._$yW["userData"] = _$f3(_$cc, _$cV);
            _$nI["call"](_$c7, _$cc, _$cV);
            _$gL["call"](_$c7, _$cc, _$cV);
        }
        if (_$cV !== _$u4) {} else {
            if (_$jb && ((window["openDatabase"] && _$c7._$yW["dbData"] === _$u4) || (_$ta && (_$c7._$yW["idbData"] === _$u4 || _$c7._$yW["idbData"] === ''))) && _$sY++ < _$c7._$u2["tests"]) { setTimeout(function() { _$vI["call"](_$c7, _$cc, _$cV, _$hr, _$sY, _$hA); }, 20); return; }
            var _$rf = _$c7._$yW,
                _$c3 = [],
                _$cf = 0,
                _$cJ, _$n5;
            _$c7._$yW = {};
            for (_$n5 in _$rf)
                if (_$rf[_$n5] && _$rf[_$n5] !== null && _$rf[_$n5] != _$u4) _$c3[_$rf[_$n5]] = _$c3[_$rf[_$n5]] === _$u4 ? 1 : _$c3[_$rf[_$n5]] + 1;
            for (_$n5 in _$c3)
                if (_$c3[_$n5] > _$cf) {
                    _$cf = _$c3[_$n5];
                    _$cJ = _$n5;
                }
            if (_$cJ !== _$u4 && (_$hA === _$u4 || _$hA != true)) _$c7["set"](_$cc, _$cJ);
            if (typeof _$hr === "function") _$hr(_$cJ, _$rf);
        }
    }
    _$wQ = _$xs;

    function _$kc(_$cc, _$cV) {
        try {
            if (_$cV !== _$u4) _$qm = _$s4(_$qm, _$cc, _$cV);
            else return _$bX(_$cc, _$qm);
        } catch (_$hr) {; }
    }
    _$xs["prototype"]["get"] = function(_$cc, _$cV, _$hr, _$sY) { _$vI["call"](this, _$cc, _$u4, _$cV, _$hr, _$sY); };

    function _$sK(_$cc, _$cV) {
        if (_$ei) try {
            var _$hr = _$t6();
            if (_$cV !== _$u4) _$ei[_$hr][_$cc] = _$cV;
            else return _$ei[_$hr][_$cc];
        } catch (_$sY) {}
    }
    _$xs["prototype"]["set"] = function(_$cc, _$cV) { _$vI["call"](this, _$cc, _$cV, _$u4); };

    function _$f3(_$cc, _$cV) {
        try {
            var _$hr = _$sA("div", "userdata_el", 1);
            if (_$hr["addBehavior"]) {
                _$hr["style"]["behavior"] = "url(#default#userdata)";
                if (_$cV !== _$u4) {
                    _$hr["setAttribute"](_$cc, _$cV);
                    _$hr["save"](_$cc);
                } else { _$hr["load"](_$cc); return _$hr["getAttribute"](_$cc); }
            }
        } catch (_$sY) {}
    };

    function _$t6() { return window[_$bm][_$lC][_$iR](/:\d+/, ''); };
}());
_$w4["prototype"] = new function() {
    this._$yq = function() {
        this._$yR = this._$zn["slice"](0);
        this._$aP = [];
        this._$ys = 0;
    };

    function _$i2(_$pY, _$ei) { return (_$ei << _$pY) | (_$ei >>> 32 - _$pY); }
    this._$wV = function(_$pY) {
        if (typeof _$pY === "string") _$pY = _$jg(_$pY);
        var _$ei = this._$aP = this._$aP["concat"](_$pY);
        this._$ys += _$pY["length"];
        while (_$ei["length"] >= 64) this._$zw(_$xO(_$ei["splice"](0, 64)));
        return this;
    };

    function _$nd(_$pY, _$ei, _$l1, _$ta) {
        if (_$pY <= 19) return (_$ei & _$l1) | (~_$ei & _$ta);
        else if (_$pY <= 39) return _$ei ^ _$l1 ^ _$ta;
        else if (_$pY <= 59) return (_$ei & _$l1) | (_$ei & _$ta) | (_$l1 & _$ta);
        else if (_$pY <= 79) return _$ei ^ _$l1 ^ _$ta;
    }
    this._$wr = function() {
        var _$pY, _$ei = this._$aP,
            _$l1 = this._$yR,
            _$ta = [];
        _$ei.push(0x80);
        for (_$pY = _$ei["length"] + 2 * 4; _$pY & 0x3f; _$pY++) _$ei.push(0);
        while (_$ei["length"] >= 64) this._$zw(_$xO(_$ei["splice"](0, 64)));
        _$ei = _$xO(_$ei);
        _$ei.push(Math["floor"](this._$ys * 8 / 0x100000000));
        _$ei.push(this._$ys * 8 | 0);
        this._$zw(_$ei);
        this._$yq();
        _$bb(_$l1, _$ta);
        return _$ta;
    };
    this._$zn = [0x67452301, 0xEFCDAB89, 0x98BADCFE, 0x10325476, 0xC3D2E1F0];
    this._$zf = [0x5A827999, 0x6ED9EBA1, 0x8F1BBCDC, 0xCA62C1D6];
    this._$zw = function(_$pY) {
        var _$ei, _$l1, _$ta, _$qm, _$eB, _$lg, _$ff, _$xs = _$pY["slice"](0),
            _$vI = this._$yR;
        _$ta = _$vI[0];
        _$qm = _$vI[1];
        _$eB = _$vI[2];
        _$lg = _$vI[3];
        _$ff = _$vI[4];
        for (_$ei = 0; _$ei <= 79; _$ei++) {
            if (_$ei >= 16) _$xs[_$ei] = _$i2(1, _$xs[_$ei - 3] ^ _$xs[_$ei - 8] ^ _$xs[_$ei - 14] ^ _$xs[_$ei - 16]);
            _$l1 = (_$i2(5, _$ta) + _$nd(_$ei, _$qm, _$eB, _$lg) + _$ff + _$xs[_$ei] + this._$zf[Math["floor"](_$ei / 20)]) | 0;
            _$ff = _$lg;
            _$lg = _$eB;
            _$eB = _$i2(30, _$qm);
            _$qm = _$ta;
            _$ta = _$l1;
        }
        _$vI[0] = (_$vI[0] + _$ta) | 0;
        _$vI[1] = (_$vI[1] + _$qm) | 0;
        _$vI[2] = (_$vI[2] + _$eB) | 0;
        _$vI[3] = (_$vI[3] + _$lg) | 0;
        _$vI[4] = (_$vI[4] + _$ff) | 0;
    };
}();
$_ts["t__"] = _$jn;
var _$xx;
var _$yn = [],
    _$xW = 0,
    _$bH = 0,
    _$sM = 0,
    _$yo = 0,
    _$ye = 0,
    _$yN = 0,
    _$ir, _$sZ = 2,
    _$bZ = 0;
(function() {
    var _$sY = 0.05,
        _$nx = 50.0,
        _$ea = 10,
        _$tv = 200.0,
        _$uO = 5000,
        _$qX = 4,
        _$df = 350,
        _$rZ = 70;

    function _$cJ(_$ex, _$bo, _$fw, _$dM) { return Math["sqrt"]((_$ex - _$fw) * (_$ex - _$fw) + (_$bo - _$dM) * (_$bo - _$dM)); }
    var _$dk = -1;

    function _$aF() {
        var _$ex = null;
        var _$bo = 0;
        var _$fw = 0;
        var _$dM = 0;
        var _$tW = 0;
        var _$sV = [];
        _$kc++;
        for (; !_$bV._$yC(); _$bV._$xy()) {
            var _$ek = _$bV._$zl();
            if (_$uv != _$ek.et) break;
            if (_$ex) {
                if (_$cV(_$ek, _$ex)) continue;
                _$tW += (_$fw = _$cJ(_$ek.x, _$ek.y, _$ex.x, _$ex.y));
                _$sV[_$bo++] = _$fw;
                dv = _$fw / (_$ex.ts - _$ek.ts);
                if (dv > _$nx) {
                    _$sK++;
                    _$dE += (dv / _$nx) - 1;
                }
                if (_$fw > _$tv) {
                    _$f3++;
                    _$nI += (_$fw / _$tv) - 1;
                }
            }
            _$dM = _$tW;
            _$xs += _$bo;
            _$ex = _$ek;
        }
        if (_$bo > 0) _$tW = _$dM / _$bo;
        var _$nH = 0;
        if (_$bo > 1) {
            for (var _$rN = 0; _$rN < _$bo; ++_$rN) _$nH += (_$sV[_$rN] - _$tW) * (_$sV[_$rN] - _$tW);
            _$nH = Math["sqrt"](_$nH / _$bo);
            if (_$nH < _$qX) _$bW += _$px(_$nH, _$bo, _$dM);
        } else _$vI++;
    }
    var _$uv = 0;

    function _$c3(_$ex, _$bo) {
        switch (_$ex) {
            case _$hr:
            case _$hA:
            case _$jb:
            case _$c7:
            case _$rf:
                _$eB++;
                break;
            default:
                break;
        }
        if (_$dk == _$ei) { _$ei = _$bo; return; }
        if (_$dk == _$l1) {
            _$l1 = _$bo - _$ei;
            _$ei = _$bo;
            return;
        }
        var _$fw = 1;
        var _$dM = _$bo - _$ei;
        if (_$dM > _$uO) {;
            _$ei = _$bo;
            _$l1 = _$dk;
            _$fw = 0;
            return;
        }
        if (_$fw) { _$qm++; if (Math["abs"](_$dM - _$l1) < _$ea) _$ta++; }
        _$ei = _$bo;
        _$l1 = _$dM;
    }
    var _$of = 1;

    function _$sA(_$ex, _$bo, _$fw) {
        this.et = _$fw;
        this.x = _$ex.x;
        this.y = _$ex.y;
        this.ts = _$bo;
        this["keyCode"] = _$ex["keyCode"];
    }
    var _$pa = 2;

    function _$n5(_$ex, _$bo, _$fw, _$dM) { return Math["acos"]((_$ex * _$fw + _$bo * _$dM) / (Math["sqrt"]((_$ex * _$ex) + (_$bo * _$bo)) * Math["sqrt"]((_$fw * _$fw) + (_$dM * _$dM)))); }
    var _$t4 = 3;

    function _$uB(_$ex, _$bo) {;
        var _$fw = _$bo - _$ex;
        _$t6++;
        if (_$fw > _$rZ && _$fw < _$df) _$s4++;
        if (_$gn < _$s2) {
            _$wy[_$gn++] = _$fw;
            _$au += _$fw;
            var _$dM = 0;
            var _$tW = _$au / _$gn;
            for (var _$sV = 0; _$sV < _$gn; ++_$sV) _$dM += (_$wy[_$sV] - _$tW) * (_$wy[_$sV] - _$tW);
            _$dM = Math["sqrt"]((1 / _$gn) * _$dM);
            if (_$dM < 3 && _$dM > 0) _$bX = 2;
        }
    }
    var _$bF = 4;

    function _$cV(_$ex, _$bo) { if (_$ex.x == _$bo.x && _$ex.y == _$bo.y) return true; return false; }
    var _$fP = 5;

    function _$oo() {
        var _$ex = 500;
        var _$bo = 0;
        var _$fw = 0;
        var _$dM = [];
        var _$tW = {};
        _$tW._$yY = function() { return ((_$fw + 1) % _$ex == _$bo); };
        _$tW._$yC = function() { return _$fw == _$bo; };
        _$tW._$wc = function() { if (this._$yC()) return null; return _$dM[_$bo]; };
        _$tW._$zl = function() { if (this._$yC()) return null; return _$dM[(_$fw - 1 + _$ex) % _$ex]; };
        _$tW._$y4 = function(_$sV) {
            if (!this._$yY()) {
                _$dM[_$fw] = _$sV;
                _$fw = (_$fw + 1) % _$ex;
            }
        };
        _$tW._$yM = function() { if (!this._$yC()) _$bo = (_$bo + 1) % _$ex; };
        _$tW._$xy = function() { if (!this._$yC()) _$fw = (_$fw - 1 + _$ex) % _$ex; };
        _$tW._$xw = function() { return (_$fw - _$bo + _$ex) % _$ex; };
        _$tW._$zr = function() {
            var _$sV = _$bo;
            while (_$sV != _$fw) {
                var _$ek = _$dM[_$sV];
                _$sV = (_$sV + 1) % _$ex;
            }
        };
        return _$tW;
    }
    var _$as = -1;

    function _$px(_$ex, _$bo, _$fw) {
        var _$dM = 500;
        var _$tW = 0;
        var _$sV = 0;
        if (_$fw >= _$dM) _$tW = 1;
        else _$tW = parseInt(_$fw / _$dM * 10) / 10;
        var _$ek = [0.2, 0.6, 1, 2, 4];
        var _$nH = [30, 15, 5, 3, 1];
        for (var _$rN = 0; _$rN < _$ek["length"]; ++_$rN)
            if (_$ex < _$ek[_$rN]) { _$sV = _$nH[_$rN] * _$tW; break; }
        _$sV = parseInt(_$sV);
        if (_$sV <= 1) _$sV = 0;
        return _$sV;
    }
    var _$l4 = 0;

    function _$tV(_$ex, _$bo) {
        var _$fw = 0;
        if (_$ex["timeStamp"]) _$fw = parseInt(_$ex["timeStamp"] + 0.5);
        else _$fw = _$ws();
        if (_$fP == _$bo) { _$c3(_$ex["keyCode"], _$fw); return; }
        switch (_$i2) {
            case _$l4:
                if (_$uv == _$bo || _$t4 == _$bo) _$i2 = _$l4;
                else if (_$bF == _$bo) _$i2 = _$sw;
                else if (_$of == _$bo) _$i2 = _$uo;
                else _$i2 = _$as;
                break;
            case _$sw:
                if (_$t4 == _$bo) _$i2 = _$oh;
                else _$i2 = _$as;
                break;
            case _$oh:
                if (_$uv == _$bo) _$i2 = _$l4;
                else _$i2 = _$as;
                break;
            case _$uo:
                if (_$pa == _$bo) _$i2 = _$b3;
                else _$i2 = _$uo;
                break;
            case _$b3:
                if (_$uv == _$bo) _$i2 = _$l4;
                else if (_$of == _$bo) _$i2 = _$uo;
                else if (_$bF == _$bo) _$i2 = _$pr;
                else _$i2 = _$as;
                break;
            case _$pr:
                if (_$t4 == _$bo) _$i2 = _$dy;
                else _$i2 = _$as;
                break;
            case _$dy:
                if (_$uv == _$bo) _$i2 = _$l4;
                else _$i2 = _$as;
                break;
        }
        if (_$as == _$i2) { _$k6 = 255; return; }
        if (_$bV._$yY()) _$bV._$yM();
        var _$dM = new _$sA(_$ex, _$fw, _$bo);
        _$bV._$y4(_$dM);
        if (_$oh == _$i2) _$cf();
        else if (_$uo == _$i2) {
            var _$tW = _$bV._$zl();
            _$nd = _$tW.ts;
            _$bV._$xy();
            if (_$l4 == _$pY) _$aF();
        } else if (_$b3 == _$i2) {
            _$bV._$xy();
            _$uB(_$nd, _$fw);
            _$cc();
        } else if (_$dy == _$i2) _$bV._$xy();
        else if (_$pr == _$i2) _$bV._$xy();
        _$pY = _$i2;
    }
    var _$sw = 1;

    function _$cc() {
        var _$ex = 0;
        var _$bo = 0;
        if (_$eB > 0) { _$ex++; }
        var _$fw = 0;
        if (_$qm > 0) _$fw = _$ta / _$qm;
        if (_$fw > 0.2) _$bo += parseInt((_$fw - 0.2) * 10);
        _$fw = _$vI / _$kc;
        var _$dM = 0;
        if (_$fw > 0.5) _$dM = 20;
        else if (_$fw > 0.3) _$dM = 10;
        if (_$fw > 0) {;
            _$bo += parseInt(_$fw * _$dM);
        };
        _$bo += _$bW;
        if (_$f3 > 0) _$bo += parseInt(_$nI / _$f3);
        if (_$sK > 0) _$bo += parseInt(_$dE / _$sK);
        _$fw = _$s4 / _$t6;
        if (_$t6 > 0)
            if (_$fw < 0.7) { _$bo += parseInt((1 - _$fw - 0.3) * 10); };
        _$bo += _$bX;
        if (_$bo > _$ex) _$bo -= _$ex;
        else _$bo = 0;
        if (_$bo >= 255) _$bo = 254;
        _$k6 = _$bo;
    }
    var _$oh = 2;

    function _$cf() {
        var _$ex = _$bV._$zl();
        _$bV._$xy();
        var _$bo = _$bV._$zl();
        _$bV._$xy();
        if (_$cV(_$ex, _$bo)) _$ff++;
        else {
            _$lg++;
            _$aF();
            _$cc();
        }
    }
    var _$uo = 3;
    var _$b3 = 4;
    var _$pr = 5;
    var _$dy = 6;
    var _$bV = _$oo();
    var _$k6 = 0;
    var _$nd = 0;
    var _$i2 = 0,
        _$pY = _$dk;
    var _$ei = _$dk,
        _$l1 = _$dk,
        _$ta = 0,
        _$qm = 0,
        _$eB = 0,
        _$lg = 0,
        _$ff = 0,
        _$xs = 0,
        _$vI = 0,
        _$kc = 0,
        _$bW = 0,
        _$sK = 0,
        _$dE = 0,
        _$f3 = 0,
        _$nI = 0,
        _$gL = 0,
        _$s4 = 0,
        _$bX = 0,
        _$t6 = 0;
    _$xx = function() { return _$k6; };
    _$vV(document, "mousemove", function(_$ex) { _$tV(_$ex, _$uv); });
    _$vV(document, "mousedown", function(_$ex) { _$tV(_$ex, _$of); });
    _$vV(document, "mouseup", function(_$ex) { _$tV(_$ex, _$pa); });
    _$vV(document, "mouseover", function(_$ex) { _$tV(_$ex, _$t4); });
    _$vV(document, "mouseout", function(_$ex) { _$tV(_$ex, _$bF); });
    _$vV(document, "keydown", function(_$ex) { _$tV(_$ex, _$fP); });
    var _$hr = 20;
    var _$hA = 8;
    var _$jb = 37;
    var _$c7 = 39;
    var _$rf = 16;
    var _$s2 = 100;
    var _$wy = [];
    var _$gn = 0;
    var _$au = 0;
}());
var _$aA;
var _$zz = "B_";
_$a7();
_$wx();
var _$op = 0,
    _$yv = 0,
    _$yp = 0,
    _$yx = 0;
var _$xu = 0,
    _$yG = 0,
    _$uX = 0,
    _$er = 0;
var _$oN = 0,
    _$tT = 0,
    _$fn = 0;
var _$xD;
var _$yH, _$tp, _$w3;
var _$t1;
var _$eH, _$gq, _$xv;
var _$a8;
var _$bN;
var _$vE;
var _$yu = 0;
var _$yl = 0;
var _$wn = 0;
var _$xt, _$wE;
var _$eT, _$rs, _$uf;
window["fontList"] = _$a9;
(function() {
    var _$nd = [];
    window["$b_onBridgeReady"] = function(_$i2) {
        if (window["$b_callHandler"]) _$i2();
        else _$nd.push(_$i2);
    };
    window["$b_setup"] = function() {
        if (window["$b_callHandler"]) return;
        var _$i2 = window["$b_platform"] == "android";
        var _$pY, _$ei = {};
        var _$l1 = 1;
        var _$ta = [];
        window["$b_callHandler"] = function(_$lg, _$ff, _$xs) {
            if (!_$pY) {
                _$pY = document["createElement"]("iframe");
                _$pY["style"]["display"] = "none";
                document["documentElement"]["appendChild"](_$pY);
            }
            var _$vI = "cb_" + (_$l1++) + '_' + new Date()["getTime"]();
            var _$kc = { 'func': _$lg, 'data': _$ff, 'callback': _$vI };
            _$ei[_$vI] = _$xs;
            if (_$i2) _$pY["src"] = "jbscheme://" + JSON["stringify"](_$kc);
            else {
                _$ta.push(_$kc);
                _$pY["src"] = "jbscheme://queue_has_message";
            }
        };
        window["$b_fetchQueue"] = function() {
            var _$lg = JSON["stringify"](_$ta);
            _$ta = [];
            return _$lg;
        };
        window["$b_onNativeResponse"] = function(_$lg, _$ff) {
            var _$xs = _$ei[_$lg];
            if (_$xs) {
                _$xs(_$ff);
                delete _$ei[_$lg];
            }
        };
        for (var _$qm = 0; _$qm < _$nd["length"]; _$qm++) {
            var _$eB = _$nd[_$qm];
            _$eB();
        }
        _$nd = [];
    };
    if (window["$b_platform"]) window["$b_setup"]();
}());
_$um["prototype"] = new function() {
    this._$uw = function(_$nd, _$i2) {
        var _$pY = Math["floor"](_$nd["length"] / 16),
            _$ei, _$l1 = [],
            _$ta = [],
            _$qm = 16 - (_$nd["length"] % 16),
            _$eB;
        if (_$i2) {
            _$eB = _$e4(16);
            _$ta = _$eB["slice"](0);
        }
        for (_$ei = 0; _$ei < _$pY; _$ei++) _$l1.push(_$nd["slice"](_$ei * 16, _$ei * 16 + 16));
        var _$lg = _$nd["slice"](_$pY * 16);
        for (_$ei = 0; _$ei < _$qm; _$ei++) _$lg.push(_$qm);
        _$l1.push(_$lg);
        for (_$ei = 0; _$ei < _$l1["length"]; _$ei++) {
            this._$e3(_$eB ? _$s0(_$l1[_$ei], _$eB) : _$l1[_$ei], _$ta);
            _$eB = _$ta["slice"](_$ta["length"] - 16);
        }
        return _$ta;
    };
    this._$yI = function(_$nd, _$i2) {;
        var _$pY, _$ei, _$l1, _$ta, _$qm = [],
            _$eB = [],
            _$lg, _$ff;
        if (_$i2) {
            _$ff = _$nd["slice"](0, 16);
            _$nd = _$nd["slice"](16);
        }
        _$pY = Math["floor"](_$nd["length"] / 16);
        for (_$ei = 0; _$ei < _$pY; _$ei++) {
            _$l1 = [];
            _$ta = _$nd["slice"](_$ei * 16, _$ei * 16 + 16);
            this._$za(_$ta, _$l1);
            _$qm.push(_$ff ? _$s0(_$l1, _$ff) : _$l1);
            _$ff = _$ta;
        }
        _$l1 = _$qm[_$pY - 1];
        _$lg = _$l1[15];
        _$l1["splice"](16 - _$lg, _$lg);
        for (_$ei = 0; _$ei < _$pY; _$ei++) _$eB = _$eB["concat"](_$qm[_$ei]);
        return _$eB;
    };
    this._$e3 = function(_$nd, _$i2) { this._$y7(_$nd, 0, _$i2); };
    this._$za = function(_$nd, _$i2) { this._$y7(_$nd, 1, _$i2); };
    this._$yE = [
        [
            [],
            [],
            [],
            [],
            []
        ],
        [
            [],
            [],
            [],
            [],
            []
        ]
    ];
    this._$y5 = function() {
        var _$nd = this._$yE[0],
            _$i2 = this._$yE[1],
            _$pY = _$nd[4],
            _$ei = _$i2[4],
            _$l1, _$ta, _$qm, _$eB = [],
            _$lg = [],
            _$ff, _$xs, _$vI, _$kc, _$bW, _$sK;
        for (_$l1 = 0; _$l1 < 256; _$l1++) _$lg[(_$eB[_$l1] = _$l1 << 1 ^ (_$l1 >> 7) * 283) ^ _$l1] = _$l1;
        for (_$ta = _$qm = 0; !_$pY[_$ta]; _$ta ^= _$ff || 1, _$qm = _$lg[_$qm] || 1) {
            _$kc = _$qm ^ _$qm << 1 ^ _$qm << 2 ^ _$qm << 3 ^ _$qm << 4;
            _$kc = _$kc >> 8 ^ _$kc & 255 ^ 99;
            _$pY[_$ta] = _$kc;
            _$ei[_$kc] = _$ta;
            _$vI = _$eB[_$xs = _$eB[_$ff = _$eB[_$ta]]];
            _$sK = _$vI * 0x1010101 ^ _$xs * 0x10001 ^ _$ff * 0x101 ^ _$ta * 0x1010100;
            _$bW = _$eB[_$kc] * 0x101 ^ _$kc * 0x1010100;
            for (_$l1 = 0; _$l1 < 4; _$l1++) {
                _$nd[_$l1][_$ta] = _$bW = _$bW << 24 ^ _$bW >>> 8;
                _$i2[_$l1][_$kc] = _$sK = _$sK << 24 ^ _$sK >>> 8;
            }
        }
        for (_$l1 = 0; _$l1 < 5; _$l1++) {
            _$nd[_$l1] = _$nd[_$l1]["slice"](0);
            _$i2[_$l1] = _$i2[_$l1]["slice"](0);
        }
    };
    this._$y7 = function(_$nd, _$i2, _$pY) {
        _$nd = _$xO(_$nd);
        var _$ei = this._$zf[_$i2],
            _$l1 = _$nd[0] ^ _$ei[0],
            _$ta = _$nd[_$i2 ? 3 : 1] ^ _$ei[1],
            _$qm = _$nd[2] ^ _$ei[2],
            _$eB = _$nd[_$i2 ? 1 : 3] ^ _$ei[3],
            _$lg, _$ff, _$xs, _$vI = _$ei["length"] / 4 - 2,
            _$kc, _$bW = 4,
            _$sK = [0, 0, 0, 0],
            _$dE = this._$yE[_$i2],
            _$f3 = _$dE[0],
            _$nI = _$dE[1],
            _$gL = _$dE[2],
            _$s4 = _$dE[3],
            _$bX = _$dE[4];
        for (_$kc = 0; _$kc < _$vI; _$kc++) {
            _$lg = _$f3[_$l1 >>> 24] ^ _$nI[_$ta >> 16 & 255] ^ _$gL[_$qm >> 8 & 255] ^ _$s4[_$eB & 255] ^ _$ei[_$bW];
            _$ff = _$f3[_$ta >>> 24] ^ _$nI[_$qm >> 16 & 255] ^ _$gL[_$eB >> 8 & 255] ^ _$s4[_$l1 & 255] ^ _$ei[_$bW + 1];
            _$xs = _$f3[_$qm >>> 24] ^ _$nI[_$eB >> 16 & 255] ^ _$gL[_$l1 >> 8 & 255] ^ _$s4[_$ta & 255] ^ _$ei[_$bW + 2];
            _$eB = _$f3[_$eB >>> 24] ^ _$nI[_$l1 >> 16 & 255] ^ _$gL[_$ta >> 8 & 255] ^ _$s4[_$qm & 255] ^ _$ei[_$bW + 3];
            _$bW += 4;
            _$l1 = _$lg;
            _$ta = _$ff;
            _$qm = _$xs;
        }
        for (_$kc = 0; _$kc < 4; _$kc++) {
            _$sK[_$i2 ? 3 & -_$kc : _$kc] = _$bX[_$l1 >>> 24] << 24 ^ _$bX[_$ta >> 16 & 255] << 16 ^ _$bX[_$qm >> 8 & 255] << 8 ^ _$bX[_$eB & 255] ^ _$ei[_$bW++];
            _$lg = _$l1;
            _$l1 = _$ta;
            _$ta = _$qm;
            _$qm = _$eB;
            _$eB = _$lg;
        }
        _$bb(_$sK, _$pY);
    };
}();
(function() {
    var _$nd = window["navigator"];

    function _$qm(_$xs) {
        var _$vI, _$kc;
        if (_$xs instanceof window["Array"]) _$vI = _$xs;
        if (Array["from"]) _$vI = Array["from"](_$xs);
        else { _$vI = new Array(_$xs["length"]); for (_$kc = 0; _$kc < _$xs["length"]; ++_$kc) _$vI[_$kc] = _$xs[_$kc]; };
        return _$vI;
    }
    var _$i2 = !!_$nd["platform"] && /iPad|iPhone|iPod/ ["test"](_$nd["platform"]);

    function _$eB() {
        var _$xs;
        var _$vI = window["navigator"]["language"] || window["navigator"]["browserLanguage"];
        if (_$vI === "zh-CN") _$xs = _$zN("_tCbyRDtiXFzNibfz8bwLXK67X84O5PPj58BL8FVX1uL.4I9XE6LNLoLBNH2fFUb23dbfxd9B_obGFdbPxMvG.v2f4B9X4B9BRUN944bOjVf");
        else _$xs = 'Warning:We have detected that this page has been modified in flight, please don\'t input any sensitive information or click on this page.';
        window["alert"](_$xs);
    }
    if (window["Uint8Array"]) {
        var _$ei = window["Uint8Array"]["prototype"];
        if (!_$ei["slice"]) _$ei["slice"] = function(_$xs, _$vI) {
            if (this["length"] === 0) return this;
            _$xs = (_$xs + this["length"]) % this["length"];
            _$vI = _$vI || this["length"];
            return this["subarray"](_$xs, _$vI);
        };
    };

    function _$l1() {
        var _$xs;
        if (window["XMLHttpRequest"]) {
            _$xs = new window["XMLHttpRequest"]();
            _$xs["open"] = _$jm || _$xs["open"];
            _$xs["send"] = _$hf || _$xs["send"];
        } else try { _$xs = new _$zX("Microsoft.XMLHTTP"); } catch (_$vI) {}
        return _$xs;
    };

    function _$lg(_$xs) {
        var _$vI, _$kc, _$bW;
        try {
            _$vI = _$xs["slice"](_$pY(_$xs, '\n' ["charCodeAt"](0)));
            _$vI = String.fromCharCode["apply"](this, _$vI);
            _$bW = _$vI["lastIndexOf"]('\'');
            _$kc = _$vI["lastIndexOf"]('\'', _$bW - 1) + 1;
            _$vI = _$vI["substr"](_$kc, _$bW - _$kc);
            _$vI = _$iW(_$vI, _$ly());
            _$vI = String.fromCharCode["apply"](this, _$vI);
            _$vI = _$aK(_$vI);
        } catch (_$sK) {; }
        return _$vI;
    }
    if ((_$bS & 4) && !_$i2 && (_$jd & 1)) _$vV(window, "load", function() { setTimeout(_$ff, 0); });

    function _$ff() {
        var _$xs = _$l1();
        _$xs["open"]["call"](_$xs, "GET", _$bJ()["href"], true);
        if (!_$zG || _$zG > 9) _$xs["responseType"] = "arraybuffer";
        _$xs["setRequestHeader"]("X-sOYOcALfiiw", '1');
        _$xs["send"]["call"](_$xs);
        _$xs["onreadystatechange"] = function() {
            if (_$xs["readyState"] == 4 && _$xs["status"] == 200) {
                var _$vI;
                var _$kc;
                if (!_$zG || _$zG > 9) _$kc = new window["Uint8Array"](_$xs["response"]);
                else if (_$zG >= 5) _$kc = new window["VBArray"](_$xs["responseBody"])["toArray"]();
                else {; return; }
                var _$bW = _$lg(_$kc);
                var _$sK = _$wZ(_$ta(_$kc));
                if (_$bW !== _$sK) {;
                    _$xg |= 1;
                    _$dW(9);
                    if (_$bS & 8) _$eB();
                } else;
            }
        };
    }

    function _$ta(_$xs) { var _$vI; if (_$xs instanceof window["Array"] || _$xs instanceof window["Uint8Array"]) { _$vI = _$pY(_$xs, '\n' ["charCodeAt"](0)); if (_$vI == -1) return _$xs; return _$qm(_$xs["slice"](0, _$vI)); } else; }

    function _$pY(_$xs, _$vI, _$kc) {
        _$kc = _$kc || _$xs["length"] - 1;
        if (_$xs["lastIndexOf"] && typeof _$xs["lastIndexOf"] === "function") return _$xs["lastIndexOf"](_$vI, _$kc);
        else {
            if (_$xs["length"] === 0) return -1;
            for (; _$kc >= 0; --_$kc)
                if (_$xs[_$kc] === _$vI) break;
            return _$kc;
        }
    }
})();
var _$zF = "MmEwMD";
var _$zY = 64;
var _$zd = 100;
var _$r2 = 0;
_$bd();
_$ui();
var _$xF, _$tQ = {};
var _$jm, _$hf;
var _$fz, _$wF;
_$wv();






function _$gK(_$nd, _$i2) {; if (_$nd["startsWith"]) return _$nd["startsWith"](_$i2); return _$nd["substr"](0, _$i2["length"]) === _$i2; }

function _$a7() {
    var _$nd = window["navigator"],
        _$i2;
    var _$pY = _$nd["userAgent"];
    if (_$nd["standalone"] !== _$u4) {
        _$ps |= 1073741824;
        _$ps |= 1048576;
        _$ps |= 67108864;
        if (_$ro(window, "$PreUCBrowserClassic,UCBrowserMessageCenter")) _$cW(15);
        else if (_$pY["indexOf"]("MicroMessenger") != -1) _$cW(22);
        else if (_$ro(window, "__firefox__,_firefox_ReaderMode")) _$cW(2);
        else if (_$ro(window, "__mttCreateFrame,mttCumstomJS")) _$cW(16);
        else if (_$ro(window, "__crWeb,__gCrWeb")) _$cW(1);
        else if (_$ro(window, "SeMobFillFormTool,SogouMse") || _$pY["lastIndexOf"]("Sogou") != -1) _$cW(21);
        else if ((/[iPhone|iPod|iPad]\sOS\s10/ ["test"](_$pY) && window["ApplePaySession"] == _$u4) || _$pY["indexOf"]("Safari") == -1) _$cW(23);
        else _$cW(3);
        return;
    }
    var _$ei = _$vB();
    if (_$ei >= 6) {
        _$oG(524288, _$ei);
        if (_$ei >= 10)
            if (!window["indexedDB"] && (window["PointerEvent"] || window["MSPointerEvent"])) _$i2 = 1;
    }
    if (_$ro(window, "msCredentials")) { _$oG(8388608, 4); if (!window["indexedDB"]) _$i2 = 1; }
    if (_$nd["webkitPersistentStorage"]) {
        _$s8(16777216);
        if (_$ro(window, "browser_parameters,item") || !_$ro(window, "openDatabase")) _$cW(20);
        else if (_$ro(window, "FaveIconJavaInterface,jesion")) _$cW(17);
        else if (_$pY["indexOf"](" OPR/") !== -1) _$cW(19);
        else _$cW(1);
        if (window["chrome"] && !window["chrome"]["runtime"])
            if (!window["chrome"]["webstore"]) {} else if (window["onautocomplete"] !== _$u4 && window["document"]["onautocomplete"] !== _$u4 && !window["PerformanceObserver"] && !window["PerformanceObserverEntryList"]) _$cW(24);
        else if (window["Entity"] && !window["AnalyserNode"]) {} else if (window["external"]["AddSearchProvider"] && !window["dumpAll"]) {} else if (window["external"]["GetNextReqID"] && window["external"]["GetOriginalUrl"]) {} else window._$y1 = 1;
    }
    if ("MozAppearance" in document["documentElement"]["style"]) _$oG(33554432, 2);
    if (_$ro(window, "UCWebExt,ucweb")) _$cW(15);
    else if (_$ro(window, "qb_bridge,qbbookshelf")) _$cW(16);
    else if (_$ro(window, "dolphin,dolphininfo,dolphinmeta")) _$cW(18);
    else if (_$pY["indexOf"]("MicroMessenger") != -1) _$cW(22);
    var _$l1 = window["safari"];
    if (_$l1 && _$l1["pushNotification"]) _$oG(67108864, 3);
    if (window["orientation"] !== _$u4) _$ps |= 1073741824;
    if (_$u9()) _$ps |= 2147483648;
    if (_$ro(window, "callPhantom,_phantom")) _$oG(134217728, 30);
    else if (_$ro(window, "$hook$,$$logger,$$lsp,$$lsrb")) _$oG(134217728, 33);
    else if (_$ro(window, "netsparker,__ns")) _$oG(134217728, 36);
    else if (_$ro(window, "hp_identifier")) _$oG(134217728, 34);
    else if (_$eK()) _$oG(134217728, 32);
    else if (_$ro(window, "spi_hooked,mozAnimationStartTime,mozIndexedDB,mozRequestAnimationFrame"))
        if (window["Gamepad"]) {} else _$oG(134217728, 35);
    else if (window._$y1) _$oG(134217728, 31);
    else if (window["Entity"] && !window["FileReader"]) _$oG(134217728, 37);
    else if (window["QTP_EPE_HOOK"] || window._$zp) _$oG(134217728, 38);
    _$jo(function(_$ta) { if (_$ta) _$ps |= 262144; });
}

function _$vQ(_$nd) {
    if (_$oN > 0) {
        _$tT += (_$ws() - _$oN);
        _$fn = _$tT / _$yo;
        _$oN = 0;
        _$dW(4);
    }
}

function _$r1(_$nd) { if (!localStorage) return; for (var _$i2 = 5; _$i2 < 13; _$i2++) { var _$pY = _$tz(_$i2); if (_$pY) _$nd[_$i2] = _$pY; } }

function _$a9(_$nd) {;
    _$wC("$_fh0", _$nd ? _$zQ(_$jv(_$nd)) : "");
}

function _$dq(_$nd) {
    if (_$nd["charAt"](0) !== "/") {
        _$nd = _$s9(_$nd, '?');
        var _$i2 = _$vu;
        if (!(_$jd & 1)) _$i2 = _$cr();
        if (_$zG && !(_$gK(_$i2, '/'))) _$i2 = '/' + _$i2;
        if (_$nd[0] == '') _$nd = _$i2 + _$nd[1];
        else _$nd = _$tt(_$i2) + _$nd[0] + _$nd[1];
    }
    return _$aL(_$nd);
}

function _$hm() {
    _$xF = _$uM(9);
    _$w7 = _$uM(1);
    _$uR = false;
    _$vu = _$uM(2) || _$w7;
    _$s3 = _$u6('', _$uM(3));
    _$bS = _$aK(_$vi(18));
    _$vD = _$aK(_$vi(17));
    _$jd = _$aK(_$vi(16));
    _$tQ = {}, _$qs = {};
    var _$nd = _$uM(10);
    if (_$nd) { var _$i2 = _$nd["split"](';'); for (var _$pY = 0; _$pY < _$i2["length"]; _$pY++) { var _$ei = _$it(_$i2[_$pY], "="); if (_$ei[0] && _$ei[1]) _$tQ[_$ei[0]] = _$ei[1]; } }
    var _$l1 = _$uM(11);
    if (_$l1) { var _$ta = _$l1["split"](';'); for (var _$pY = 0; _$pY < _$ta["length"]; _$pY++) { var _$qm = _$it(_$ta[_$pY], "="); if (_$qm[0] && _$qm[1]) _$qs[_$qm[0]] = _$qm[1]; } }
    _$vC = Number(_$uM(25));
    _$vN = _$ws();
}

function _$vT(_$nd, _$i2) {
    var _$pY = ["setRequestHeader", "abort", "addEventListener", "dispatchEvent", "removeEventListener", "getAllResponseHeaders", "getResponseHeader", "overrideMimeType"],
        _$ei = {},
        _$l1;

    function _$qm(_$ff) { _$ff = _$j4(_$ff, _$ei["url"], _$i2); return _$nd["send"](_$ff); };

    function _$eB(_$ff, _$xs) {
        _$ei["readyState"] = _$nd["readyState"];
        if (_$nd["readyState"] === 4) {
            _$ei["response"] = _$nd["response"];
            _$ei["responseBody"] = _$nd["responseBody"];
            _$ei["responseText"] = _$nd["responseText"];
            _$ei["responseXML"] = _$nd["responseXML"];
            _$ei["status"] = _$nd["status"];
            _$ei["statusText"] = _$nd["statusText"];
        }
        if (_$ei["onreadystatechange"]) _$ei["onreadystatechange"](_$ff, _$xs);
    }
    for (_$l1 = 0; _$l1 < _$pY["length"]; _$l1++) _$ei[_$pY[_$l1]] = _$lg(_$pY[_$l1]);

    function _$lg(_$ff) {
        return function() {
            switch (arguments["length"]) {
                case 0:
                    return _$nd[_$ff]();
                case 1:
                    return _$nd[_$ff](arguments[0]);
                case 2:
                    return _$nd[_$ff](arguments[0], arguments[1]);
                case 3:
                    return _$nd[_$ff](arguments[0], arguments[1], arguments[2]);
                default:
                    ;
            }
        };
    }
    _$ei["open"] = _$ta;

    function _$ta(_$ff, _$xs, _$vI, _$kc, _$bW) {
        if (_$i2) _$xs = _$tA(_$xs);
        else _$xs = _$v8(_$xs);
        _$ei["url"] = _$xs;
        if (_$kc && _$bW) return _$nd["open"](_$ff, _$xs, _$vI, _$kc, _$bW);
        else return _$nd["open"](_$ff, _$xs, _$vI);
    }
    _$ei["send"] = _$qm;
    _$ei["readyState"] = 0;
    _$ei["onreadystatechange"] = null;
    _$nd["onreadystatechange"] = _$eB;
    return _$ei;
}

function _$wY(_$nd) {
    var _$i2 = _$u4;
    var _$pY = '';
    var _$ei = _$qP(_$fN(_$zy));
    if (_$ei && _$ei["length"] >= _$zd) {
        _$i2 = _$ei["charAt"](0);
        var _$l1 = _$zT(_$ei["substring"](1));
        var _$ta = _$l1[_$zY + 1];
        for (var _$qm = 0; _$qm < _$zY + 1; _$qm++) _$l1[_$qm] ^= _$ta;
        _$pY = _$l1["slice"](0, _$zY + 1);
    }
    var _$eB = _$tG(_$hn());
    if (!_$i2 || _$pY["length"] != _$zY + 1 || _$eB[31] != _$pY[_$zY]) {;
        window["location"]["reload"]();
        return '';
    }
    var _$lg = _$d1();
    if (_$lg <= _$r2) { _$lg = _$r2 + 1; }
    _$r2 = _$lg;
    var _$ff = [];
    _$bb([(_$lg / 0x100000000) & 0xffffffff, _$lg & 0xffffffff], _$ff);
    var _$xs = _$sh(_$nd);
    var _$vI = _$ff["concat"](_$xs);
    var _$kc = _$uc(_$pY["concat"](_$vI));
    for (var _$qm = 0; _$qm < _$zY + 1; _$qm++) _$pY[_$qm] ^= _$kc;
    var _$bW = _$oY(_$eB);
    var _$sK = _$oY(_$tG(_$ly()));
    var _$dE = [];
    for (var _$qm = 0; _$qm < 16; _$qm++) {
        _$dE[_$qm * 2] = _$bW[_$qm];
        _$dE[_$qm * 2 + 1] = _$sK[_$qm];
    }
    var _$f3 = _$eJ(_$vI, _$dE);
    return _$i2 + _$zQ(_$pY["concat"](_$kc, _$f3));
};

function _$vi(_$nd) {
    var _$i2 = _$nd % 64;
    var _$pY = _$nd - _$i2;
    _$i2 = _$tF(_$i2);
    _$i2 ^= _$v4;
    _$pY += _$i2;
    return _$vf[_$pY];
};

function _$co(_$nd, _$i2, _$pY) {; return _$pS((_$pY - _$nd) * 65535 / (_$i2 - _$nd)); };

function _$vs(_$nd, _$i2) {
    var _$pY = localStorage || _$zZ;
    _$pY[_$nd] = _$i2;
};

function _$sl(_$nd) {
    if (_$yn["length"] < 1100) _$yn.push(_$nd["button"], _$nd.x, _$nd.y);
    _$sM++;
    _$op = _$ws();
    _$dW(3);
}

function _$t7() {
    if (_$lT) /$/.test(_$vv());
    var _$nd = new Array(32);
    for (var _$i2 = 0; _$i2 < 32; _$i2++) _$nd[_$i2] = _$i2;
    _$nd = _$rY(_$nd).split('');
    var _$pY = new Array(129);
    for (var _$i2 = 127; _$i2 < 256; _$i2++) _$pY[_$i2 - 127] = _$i2;
    _$pY = _$rY(_$pY).split('');
    _$y2 = 'I-M3DJ0rcufq%d\\1]B:b&yTo2<>HFn};X |9v`[(V#A~Z*5.Cm^OWR{SN/E6pU)K$ztL@8e,jax\'7!lQg4s+w"k?P=i_GYh'.split('');
    _$y2 = _$nd.concat(_$y2.concat(_$pY));
    _$ya = 'AmuI`,4kG^Msg!OY&/8#qN[leC2?9y:wdJ1P$Z<|; %_c"XSxoUW6]HT@}LF.0R{Ei3(-f*p~zhvnQ=7\\+\'rb)Dtj5aVB>K'.split('');
}

function _$qq() {
    var _$nd = new _$wQ();

    function _$i2(_$pY) { try { var _$ei = _$iW(_$pY, _$ly()); return _$ei; } catch (_$l1) {; } }
    _$nd["get"]("$_YWTU", function(_$pY) {
        var _$ei;
        if (_$pY) _$ei = _$i2(_$pY);
        var _$l1;
        var _$ta = _$vi(26);
        if (_$ta) _$l1 = _$i2(_$ta);
        if (_$l1 && _$ei) {
            _$xt = _$ei;
            _$nd["get"]("$_cDro", function(_$qm) {
                _$wE = parseInt(_$qm);
                _$wE = window["isNaN"](_$wE) ? 0 : _$wE;
                _$wE++;
                _$nd["set"]("$_cDro", _$wE);
            });
        } else if (_$l1) {
            _$xt = _$l1;
            _$wE = 0;
            _$nd["set"]("$_YWTU", _$ta);
            _$nd["set"]("$_cDro", _$wE);
        } else if (_$ei) {;
            _$xt = _$ei;
            _$nd["get"]("$_cDro", function(_$qm) { _$wE = _$qm; });
        } else;
    });
}

function _$gP() {
    _$a7();
    _$q5();
    if (!_$wC("$_fh0")) {
        _$wb();
        _$dr();
    }
    _$dW(2);
}

function _$s8(_$nd, _$i2) { if (_$i2 === _$u4 || _$i2) _$ps |= _$nd; };

// trim的实现
function _$ug() { return this["replace"](/^\s+|\s+$/g, ''); };

function _$tL(_$nd) {
    var _$i2;
    try {
        var _$pY = document["createElement"]("a");
        _$pY["href"] = location["href"];
        var _$ei = document["createElement"]("a");
        _$ei["href"] = _$nd;
        _$ei["href"] = _$ei["href"];
        _$i2 = _$pY["protocol"] + "//" + _$pY["host"] !== _$ei["protocol"] + "//" + _$ei["host"];
    } catch (_$l1) { _$i2 = true; }
    return _$i2;
};

function _$sh(_$nd) {
    var _$i2, _$pY;
    _$pf();
    _$cI();
    _$aZ(4, _$wB);
    _$nd = _$nd || 255;
    var _$ei = 0;
    var _$l1 = [1, _$nd];
    _$bb([_$ei, _$ps, _$xg], _$l1);
    _$l1.push(_$hT, _$bZ);
    _$d9(_$l1, _$wt());
    _$pY = _$wC("$_f0", _$vb);
    if (_$pY) {
        _$d9(_$l1, _$zT(_$pY));
        _$ei |= 1;
    }
    if (_$yn["length"] > 0 || _$yu > 0 || _$yl > 0 || _$wn > 0) {
        _$d9(_$l1, _$pS(_$xW));
        _$d9(_$l1, _$pS(_$bH));
        _$d9(_$l1, _$pS(_$sM));
        _$d9(_$l1, _$pS(_$ye));
        _$d9(_$l1, _$pS(_$yo));
        _$d9(_$l1, _$pS(_$yu));
        _$d9(_$l1, _$pS(_$yl));
        _$d9(_$l1, _$pS(_$wn));
        _$d9(_$l1, _$pS(_$yx));
        _$d9(_$l1, _$pS(_$uX));
        _$d9(_$l1, _$pS(_$fn));
        _$ei |= 2;
    }
    _$pY = _$wC("$_fh0");
    if (_$pY) {
        _$d9(_$l1, _$zT(_$pY));
        _$ei |= 4;
    }
    _$pY = _$wC("$_f1", _$sp);
    if (_$pY) {
        _$d9(_$l1, _$zT(_$pY));
        _$ei |= 8;
    }
    if (_$xD != _$u4 || _$t1 != _$u4) {
        _$d9(_$l1, _$pS(_$xD));
        _$d9(_$l1, _$pS(_$t1));
        _$ei |= 16;
    }
    if (_$a8 != _$u4) {
        _$l1.push(_$a8);
        _$d9(_$l1, _$pS(window["Math"]["round"](_$vE)));
        if (_$bN) _$xg |= 2;
        _$ei |= 32;
    }
    var _$ta = _$vz();
    if (_$ta != _$u4) {
        _$l1.push(_$ta);
        _$ei |= 64;
    }
    if (_$aA != _$u4) {
        var _$qm = window["Math"]["round"]((_$ws() - _$aA) / 100.0);
        _$d9(_$l1, _$pS(_$qm));
        _$ei |= 128;
    }
    var _$eB = _$wC("$_fr");
    if (_$eB) {
        _$d9(_$l1, _$zT(_$eB));
        _$ei |= 256;
    }
    if (_$xt && _$wE !== _$u4) {
        _$d9(_$l1, _$xt);
        _$l1.push(_$q0(_$wE));
        _$ei |= 512;
    }
    var _$lg = _$wC("$_fpn1");
    if (_$lg) try {
        _$d9(_$l1, _$zT(_$lg));
        _$ei |= 1024;
    } catch (_$ff) {}
    var _$xs = _$xx();
    if (_$xs != _$u4) {
        _$l1.push(_$xs);
        _$ei |= 2048;
    }
    try {
        _$pY = _$zT(_$wC("$_vvCI"));
        if (_$pY && _$pY["length"] === 4) {
            _$d9(_$l1, _$pY);
            _$ei |= 4096;
        }
        _$pY = _$zT(_$wC("$_JQnh"));
        if (_$pY && _$pY["length"] === 4) {
            _$d9(_$l1, _$pY);
            _$ei |= 8192;
        }
    } catch (_$ff) {}
    if (_$eH != _$u4 && _$gq != _$u4 && _$xv != _$u4) try {
        _$d9(_$l1, _$co(0, 360, _$eH));
        _$d9(_$l1, _$co(-180, 180, _$gq));
        _$d9(_$l1, _$co(-90, 90, _$xv));
        _$ei |= 16384;
    } catch (_$ff) {}
    if (_$rs != _$u4) {
        var _$vI = window["Math"]["round"]((_$rs + (_$uf ? _$ws() - _$eT : 0)) / 100.0);
        _$d9(_$l1, _$pS(_$vI));
        _$ei |= 32768;
    }
    var _$kc = [];
    _$bb([_$ei], _$kc);
    for (var _$i2 = 0; _$i2 < 4; ++_$i2) _$l1[2 + _$i2] = _$kc[_$i2];
    return _$l1;
}

function _$sJ() {
    var _$nd = document["getElementsByTagName"]("script");
    var _$i2 = _$nd[_$nd["length"] - 1];
    _$i2["parentNode"]["removeChild"](_$i2);
}


function _$wa(_$nd) {
    var _$i2 = window["ActiveXObject"];
    if (_$i2) {
        var _$pY = ["ShockwaveFlash.ShockwaveFlash", "AcroPDF.PDF", "PDF.PdfCtrl", "QuickTime.QuickTime", "rmocx.RealPlayer G2 Control", "rmocx.RealPlayer G2 Control.1", "RealPlayer.RealPlayer(tm) ActiveX Control (32-bit)", "RealVideo.RealVideo(tm) ActiveX Control (32-bit)", "RealPlayer", "SWCtl.SWCtl", "WMPlayer.OCX", "AgControl.AgControl", "Skype.Detection"];
        for (var _$ei = 0; _$ei < _$pY["length"]; _$ei++) try {
            new _$i2(_$pY[_$ei]);
            _$nd.push(_$pY[_$ei]);
        } catch (_$l1) { return null; }
    }
};

function _$nS(_$nd, _$i2) { return _$zQ(_$eJ(_$nd, _$i2)); };

function _$s0(_$nd, _$i2) {
    var _$pY = [],
        _$ei;
    for (_$ei = 0; _$ei < 16; _$ei++) _$pY.push(_$nd[_$ei] ^ _$i2[_$ei]);
    return _$pY;
};

function _$cX(_$nd, _$i2) { return _$nd[_$i2]; }


function _$u6(_$nd, _$i2) { if (_$i2) _$nd += '?' + _$i2; return _$nd; }

function _$rr(_$nd) { window["$b_callHandler"]("Z8XHj", '', _$nd); }

function _$uM(_$nd) { return _$zP(_$vi(_$nd)); }


function _$uc(_$nd) { if (typeof _$nd === "string") _$nd = _$jg(_$nd); var _$i2 = _$ds(function() { return _$xq; }); var _$pY = window[_$i2] || (window[_$i2] = _$mu()); var _$ei = 0; for (var _$l1 = 0; _$l1 < _$nd["length"]; _$l1++) _$ei = _$pY[(_$ei ^ _$nd[_$l1]) & 0xFF]; return _$ei; }

function _$v8(_$nd) {
    var _$i2 = _$sL(_$nd);
    var _$pY = '';
    if (_$i2._$xY === 1) _$pY = _$dq(_$i2._$xX);
    else if (_$i2._$xY === 2) _$pY = _$i2._$xX;
    else if (_$i2._$xY === 3) return _$nd;
    var _$ei = _$oY(decodeURIComponent(_$pY["replace"](/\+/g, "%20")));
    _$pY = _$s9(_$pY, '#');
    var _$l1 = _$pY[1];
    if (_$pY[0]["indexOf"]('?') === -1) _$pY = _$pY[0] + '?';
    else _$pY = _$pY[0] + '&';
    var _$ta = _$i2._$zj + _$pY;
    _$ta += _$kB(_$nd, _$ei);
    _$ta += _$l1;
    return _$ta;
}

function _$bd() { _$fS(); }
function _$tF(_$nd) { var _$i2 = [0, 1, 3, 7, 0xf, 0x1f]; return (_$nd >> _$gG) | ((_$nd & _$i2[_$gG]) << (6 - _$gG)); }


function _$ds(_$nd) { return _$nd["toString"]()["match"](/{\s*return\s*([A-Za-z0-9$_-]+);?\s*}/)[1]; }


function _$ud(_$nd, _$i2) { if (typeof _$nd === "string") _$nd = _$jg(_$nd); var _$pY = _$gi(_$nd, _$i2); return _$zQ(_$pY); }
function _$mu() {
    var _$nd = [];
    for (var _$i2 = 0; _$i2 < 256; ++_$i2) {
        var _$pY = _$i2;
        for (var _$ei = 0; _$ei < 8; ++_$ei)
            if ((_$pY & 0x80) !== 0) _$pY = (_$pY << 1) ^ 7;
            else _$pY <<= 1;
        _$nd[_$i2] = _$pY & 0xff;
    }
    return _$nd;
}
function _$vp(_$nd, _$i2, _$pY) { if (_$nd !== _$i2) { if (localStorage && localStorage.$d === '1') debugger; if (!_$pY) _$pY = "assert failed: " + _$nd + " is not same as " + _$i2; throw _$pY; } }
function _$s9(_$nd, _$i2) { var _$pY = _$nd["indexOf"](_$i2); if (_$pY === -1) return [_$nd, '']; return [_$nd["substr"](0, _$pY), _$nd["substr"](_$pY)]; }
function _$jv(_$nd) { return new _$w4()._$wV(_$nd)._$wr(); }

function _$ja(_$nd, _$i2) { document["cookie"] = _$nd + '=' + _$i2 + "; path=/" + _$wL(365 * 10); }

function _$fS() {
    _$vV(document, "mousedown", _$sl);
    _$vV(document, "mouseup", _$aH);
    _$vV(document, "mousemove", _$iH);
    _$vV(document, "keydown", _$wW);
    _$vV(document, "touchstart", _$v9);
    _$vV(document, "touchmove", _$vA);
    _$vV(document, "touchend", _$vQ);
    _$vV(document, "click", _$rg);
    _$vV(document, "input", _$xC);
    _$vV(document, "scroll", _$uz);
    _$vV(window, "load", _$pf);
    if (document["addEventListener"]) {
        _$vV(document, "driver-evaluate", _$pf);
        _$vV(document, "webdriver-evaluate", _$pf);
        _$vV(document, "selenium-evaluate", _$pf);
    }
    _$vV(window, "error", _$bC);
    _$vV(window, "load", _$gP);
    window["setInterval"](function() { _$dW(10); }, 50000);
    try {
        if (window["DeviceMotionEvent"] != _$u4) {
            _$xD = 0;
            window["addEventListener"]("devicemotion", _$xe, true);
        }
        if (window["DeviceOrientationEvent"] != _$u4) {
            _$t1 = 0;
            window["addEventListener"]("deviceorientation", _$aN, true);
        }
    } catch (_$nd) {}
    _$pk();
    _$vV(window, "load", function() {
        _$aA = _$ws();
        _$eT = _$ws();
        _$xj();
    });
    _$ah();
    _$qq();
    try { var _$i2 = _$wC("$_fpn1"); if (!_$i2) { _$i2 = _$vi(27); if (_$i2) _$vs("$_fpn1", _$i2); } } catch (_$nd) {}
    window["$b_onBridgeReady"](function() {
        _$rr(function(_$pY) {
            try {
                _$vs("$_fpn1", _$pY);
                _$dW(8);
            } catch (_$ei) {}
        });
    });
    _$rv();
}
function _$ly() { var _$nd = _$zT(_$vi(19) + _$c8[0] + _$to(function() { return _$ea; })); return _$wh(_$nd); }

function _$qI(_$nd, _$i2) { return _$nd["tagName"]["toLowerCase"]() == _$i2; }

function _$to(_$nd) {
    var _$i2 = _$ds(_$nd);
    if (_$gK(_$i2, "_$")) _$i2 = _$i2["substr"](2)["replace"]('$', '.');
    else _$i2 = '';
    return _$i2;
}

function _$sp() {
    try { var _$nd = document["createElement"]("canvas"); var _$i2 = _$nd["getContext"]("webgl") || _$nd["getContext"]("experimental-webgl"); } catch (_$pY) {; return; };

    function _$l1() {
        var _$gL = _$i2["getSupportedExtensions"]();
        for (var _$s4 = 0; _$s4 < _$gL["length"]; _$s4++) {
            var _$bX = _$gL[_$s4];
            var _$t6 = _$i2["getExtension"](_$bX);
            _$ta.push(_$bX);
            _$ei(_$t6);
        }
    }
    try {
        var _$ta = [];
        var _$qm = "attribute vec2 attrVertex;varying vec2 varyinTexCoordinate;uniform vec2 uniformOffset;void main(){varyinTexCoordinate=attrVertex+uniformOffset;gl_Position=vec4(attrVertex,0,1);}";
        var _$eB = "precision mediump float;varying vec2 varyinTexCoordinate;void main() {gl_FragColor=vec4(varyinTexCoordinate,0,1);}";
        var _$lg = _$i2["createBuffer"]();
        _$i2["bindBuffer"](_$i2["ARRAY_BUFFER"], _$lg);
        var _$ff = new window["Float32Array"]([-.2, -.9, 0, .4, -.26, 0, 0, .813264543, 0]);
        _$i2["bufferData"](_$i2["ARRAY_BUFFER"], _$ff, _$i2["STATIC_DRAW"]);
        _$lg["itemSize"] = 3;
        _$lg["numItems"] = 3;
        var _$xs = _$i2["createProgram"](),
            _$vI = _$i2["createShader"](_$i2["VERTEX_SHADER"]);
        _$i2["shaderSource"](_$vI, _$qm);
        _$i2["compileShader"](_$vI);
        var _$kc = _$i2["createShader"](_$i2["FRAGMENT_SHADER"]);
        _$i2["shaderSource"](_$kc, _$eB);
        _$i2["compileShader"](_$kc);
        _$i2["attachShader"](_$xs, _$vI);
        _$i2["attachShader"](_$xs, _$kc);
        _$i2["linkProgram"](_$xs);
        _$i2["useProgram"](_$xs);
        _$xs["vertexPosAttrib"] = _$i2["getAttribLocation"](_$xs, "attrVertex");
        _$xs["offsetUniform"] = _$i2["getUniformLocation"](_$xs, "uniformOffset");
        _$i2["enableVertexAttribArray"](_$xs["vertexPosArray"]);
        _$i2["vertexAttribPointer"](_$xs["vertexPosAttrib"], _$lg["itemSize"], _$i2["FLOAT"], !1, 0, 0);
        _$i2["uniform2f"](_$xs["offsetUniform"], 1, 1);
        _$i2["drawArrays"](_$i2["TRIANGLE_STRIP"], 0, _$lg["numItems"]);
        if (_$i2["canvas"] != null) _$ta.push(_$i2["canvas"]["toDataURL"]());
        _$l1();
        _$ei(_$i2);
        if (_$i2["getShaderPrecisionFormat"]) {
            var _$bW = [_$i2["VERTEX_SHADER"], _$i2["FRAGMENT_SHADER"]],
                _$sK = [_$i2["HIGH_FLOAT"], _$i2["MEDIUM_FLOAT"], _$i2["LOW_FLOAT"], _$i2["HIGH_INT"], _$i2["MEDIUM_INT"], _$i2["LOW_INT"]];
            for (var _$dE = 0; _$dE < _$bW["length"]; _$dE++)
                for (var _$f3 = 0; _$f3 < _$sK["length"]; _$f3++) {
                    var _$nI = _$i2["getShaderPrecisionFormat"](_$bW[_$dE], _$sK[_$f3]);
                    _$ta.push(_$nI["rangeMin"], _$nI["rangeMax"], _$nI["precision"]);
                }
        }
    } catch (_$pY) {; };

    function _$ei(_$gL) {
        for (var _$s4 in _$gL)
            if (_$s4["toUpperCase"]() === _$s4) {
                var _$bX = _$i2["getParameter"](_$gL[_$s4]);
                if (_$bX != _$u4) {
                    if (typeof _$bX === "number" && _$bX >= 0xFFFFFF) continue;
                    _$ta.push(_$bX);
                }
            }
    };
    return _$zQ(_$jv(_$ta.join(':')));
}

function _$bJ() { return window["location"]; }

function _$kB(_$nd, _$i2) {
    var _$pY = [];
    var _$ei = _$wY(6);
    if (_$ei) {
        _$pY = _$pY["concat"](_$i2);
        _$pY.push(_$tL(_$nd) ? 1 : 0);
        var _$l1 = _$vW + _$ei + _$xT(_$pY);
        _$l1 += _$sy(_$l1);
        return _$zF + '=' + _$l1;
    } else return _$zF + '=';
}

// 判断是否开启flash，开启返回true，关闭返回false
function _$u9() {
    var _$nd;
    try { _$nd = new window["ActiveXObject"]("ShockwaveFlash.ShockwaveFlash"); } catch (_$i2) {
        var _$pY = window["navigator"]["mimeTypes"];
        _$nd = _$pY["application/x-shockwave-flash"];
        _$nd = _$nd && _$nd["enabledPlugin"];
    }
    return _$nd !== _$u4;
}

function _$tD(_$nd) {
    var _$i2 = _$nd.split('');
    _$uA(_$i2, 0, _$i2.length, 2);
    return _$i2.join('');
}

function _$uA(_$nd, _$i2, _$pY, _$ei) {
    var _$l1 = Math.floor((_$i2 + _$pY) / 2);
    if (_$ei > 0) { _$ei--; if (_$l1 - _$i2 >= 3) _$uA(_$nd, _$i2, _$l1, _$ei); if (_$pY - _$l1 >= 3) _$uA(_$nd, _$l1, _$pY, _$ei); }
    for (var _$ta = _$i2; _$ta < _$l1; _$ta += 2) {
        var _$qm = _$nd[_$ta];
        var _$eB = _$pY - 1 - (_$ta - _$i2);
        _$nd[_$ta] = _$nd[_$eB];
        _$nd[_$eB] = _$qm;
    }
}

// _$gb()主要是加工网页元素id为“9DhefwqGPrzGxEp9hPaoag”的函数
function _$gb() {
    var _$nd = document["getElementById"]("9DhefwqGPrzGxEp9hPaoag");

    function _$eB() {
        var _$lg, _$ff;
        _$lg = _$dN(_$i2["charAt"](_$ei));
        if (_$lg < 0) {;
            _$ei++;
            _$ff = _$ei + 3;
            _$lg = 0;
            for (; _$ei < _$ff; _$ei++) _$lg = _$lg * 86 + _$dN(_$i2["charAt"](_$ei));
        } else if (_$lg < 64) _$ei++;
        else if (_$lg <= 86) {
            _$lg = (_$lg - 64) * 86 + _$dN(_$i2["charAt"](_$ei + 1)) + 64;
            _$ei += 2;
        } else;
        return _$lg;
    }
    var _$i2 = _$nd["content"];
    // _$nd["parentElement"]["removeChild"](_$nd); //这句话把9DhefwqGPrzGxEp9hPaoag元素删除了，先注释掉，便于调试
    var _$pY = _$i2["length"],
        _$ei = 0,
        _$l1, _$ta = 0;
    var _$qm = _$eB();
    _$v4 = _$aK(_$v4);
    _$gG = _$aK(_$gG);
    _$vf = new window["Array"](_$qm);
    while (_$ei < _$pY) {
        _$l1 = _$eB();
        _$vf[_$ta] = _$i2["substr"](_$ei, _$l1);
        _$ei += _$l1;
        _$ta++;
    };
}
function _$vV(_$nd, _$i2, _$pY) {
    if (_$nd["addEventListener"]) _$nd["addEventListener"](_$i2, _$pY);
    else {
        _$i2 = "on" + _$i2;
        _$nd["attachEvent"](_$i2, _$pY);
    }
}
function _$iH(_$nd) {
    if (_$yn["length"] < 1000) _$yn.push(_$nd["offsetX"], _$nd["offsetY"], _$nd.x, _$nd.y);
    _$bH++;
}
function _$jn(_$nd) {
    _$nd = _$nd["split"]("`");
    if (_$nd["length"] === 4)
        if (localStorage) {
            localStorage["$_turi"] = _$nd[0];
            localStorage["$_ttarg"] = _$nd[1];
            localStorage["$_tk1"] = _$nd[2];
            localStorage["$_tk2"] = _$nd[3];
        }
}
function _$vz() {
    var _$nd;
    var _$i2 = window["navigator"];
    var _$pY = _$i2["connection"] || _$i2["mozConnection"] || _$i2["webkitConnection"];
    if (_$pY)
        if (_$pY["type"] == "bluetooth") _$nd = 1;
        else if (_$pY["type"] == "cellular") _$nd = 2;
    else if (_$pY["type"] == "ethernet") _$nd = 3;
    else if (_$pY["type"] == "wifi") _$nd = 4;
    else if (_$pY["type"] == "wimax") _$nd = 5;
    else _$nd = 0;
    return _$nd;
}
function _$c6() { return window["Math"]["ceil"](_$ws() / 1000); }

function _$wL(_$nd) { var _$i2 = _$ws() + _$nd * 24 * 60 * 60 * 1000; return "; expires=" + new Date(_$i2)["toGMTString"](); }

function _$j4(_$nd, _$i2, _$pY) {
    _$aZ(2, _$xp(5));
    if (_$pY && (_$jd & 8) && _$nd && _$nd["length"] > 0) {
        var _$ei = _$c4(_$i2)[1];
        _$nd = _$wN(_$nd, _$ei);
    }
    return _$nd;
}
function _$xp(_$nd) {
    var _$i2 = window.Error && new window.Error();
    if (_$i2) {
        var _$pY = _$i2["stack"];
        if (!_$pY) return;
        var _$ei = _$pY["toString"]();
        var _$l1 = _$ei["split"]('\n');
        _$ei = _$l1["pop"]();
        if (_$ei === '' && _$l1["length"] > 0) _$ei = _$l1["pop"]();
        if (_$ei["indexOf"]("Object.InjectedScript.evaluate") !== -1 || _$gK(_$ei, "@debugger") || _$ei === "evaluate") { _$wd(_$nd, 1); return true; }
    }
}
function _$jo(_$nd) {
    var _$i2;
    var _$pY = function() { _$nd(true); };
    var _$ei = function() { _$nd(false); };
    try {
        var _$l1 = window["navigator"];
        if (window["webkitRequestFileSystem"] && !(_$l1["appVersion"] && /Android 4\.[0-3].+ (GT|SM|SCH)-/ ["test"](_$l1["appVersion"]))) window["webkitRequestFileSystem"](window["TEMPORARY"], 1, _$ei, _$pY);
        else if ("MozAppearance" in document["documentElement"]["style"]) {
            _$i2 = window["indexedDB"]["open"]("EkcP");
            _$i2["onerror"] = _$pY;
            _$i2["onsuccess"] = _$ei;
        } else if (window["safari"] && window["safari"]["pushNotification"]) try { window["localStorage"]["length"] ? _$ei() : (window["localStorage"].x = 1, window["localStorage"]["removeItem"]("x"), _$ei()); } catch (_$ta) { _$pY(); } else if (!window["indexedDB"] && (window["PointerEvent"] || window["MSPointerEvent"])) _$pY();
            else _$ei();
    } catch (_$ta) { _$ei(); }
}
function _$oY(_$nd) { return new _$w4()._$wV(_$nd)._$wr()["slice"](0, 16); }

function _$hn() {
    var _$nd = _$zT(_$vi(21) + _$c8[2] + _$to(function() { return _$S9; }));
    _$s8(4096, _$nd["length"] !== 32);
    _$vp(_$nd["length"], 32, "Stolen Via Net: Cookie key length is incorrect.");
    return _$wh(_$nd);
}

function _$zH(_$nd) {
    if (window["JSON"] && window["JSON"]["stringify"]) return JSON["stringify"](_$nd);

    function _$pY(_$ei) {
        var _$l1, _$ta, _$qm;
        switch (typeof _$ei) {
            case "string":
                return _$i2(_$ei);
            case "number":
                return isFinite(_$ei) ? String(_$ei) : "null";
            case "boolean":
            case "null":
                return String(_$ei);
            case "object":
                if (!_$ei) return "null";
                var _$eB = Object["prototype"]["toString"]["apply"](_$ei);
                _$qm = [];
                if (_$eB === "[object Array]") { for (_$l1 = 0; _$l1 < _$ei["length"]; _$l1 += 1) _$qm[_$l1] = _$pY(_$ei[_$l1]); return '[' + _$qm.join(',') + ']'; }
                for (_$ta in _$ei)
                    if (Object["prototype"]["hasOwnProperty"]["call"](_$ei, _$ta)) _$qm.push(_$i2(_$ta) + ':' + _$pY(_$ei[_$ta]));
                return '{' + _$qm.join(',') + '}';
        }
    }
    return _$pY(_$nd);

    function _$i2(_$ei) { var _$l1 = /[\\\"\u0000-\u001f\u007f-\u009f\u00ad\u0600-\u0604\u070f\u17b4\u17b5\u200c-\u200f\u2028-\u202f\u2060-\u206f\ufeff\ufff0-\uffff]/g; var _$ta = { '\b': '\\b', '\t': '\\t', '\n': '\\n', '\f': '\\f', '\r': '\\r', '"': '\\"', '\\': '\\\\' }; return '"' + _$ei["replace"](_$l1, function(_$qm) { var _$eB = _$ta[_$qm]; return _$eB ? _$eB : '\\u' + ("0000" + _$qm["charCodeAt"](0)["toString"](16))["slice"](-4); }) + '"'; }
}

function _$cI() {
    if (!localStorage) return;
    if (localStorage["$_ck"]) {
        var _$nd = localStorage["$_ck"];
        var _$i2 = _$vi(6);
        if (_$nd == _$i2) return;
        _$s8(16384);
    } else { _$s8(32768); }
}
function _$vy(a, b, c) { var d = []; for (var e = 0; e < c["length"]; e++) d[e] = "c[" + e + ']'; return eval("a[b](" + d.join(',') + ')'); }

function _$rg(_$nd) { _$dW(3);++_$yl; }

function _$aZ(_$nd, _$i2) { _$hT |= _$nd; if (_$i2) _$ps |= _$nd; }

function _$qY() {
    if (!localStorage) { _$dW(1); return; }
    var _$nd = _$uM(5);
    if (_$nd) {
        var _$i2 = _$fN(_$zy);
        _$ja(_$i2, _$nd);
        localStorage["$_ck"] = _$vi(6);
    } else _$cI();
}
function _$oG(_$nd, _$i2) {
    var _$pY = _$ps;
    _$s8(_$nd);
    if ((_$pY & 134217728) && _$bZ) return;
    else _$bZ = _$i2;
}
function _$cr() {
    var _$nd = document["getElementsByTagName"]("base");
    if (_$nd && _$nd["length"] > 0 && _$nd[_$nd["length"] - 1]["href"]) {
        var _$i2 = document["createElement"]('a');
        _$i2["href"] = _$nd[_$nd["length"] - 1]["href"];
        return _$i2["pathname"];
    } else return _$vu;
}
function _$iV(_$nd) {
    var _$i2 = _$nd["length"],
        _$pY = new Array(_$i2),
        _$ei, _$l1;
    for (_$ei = 0; _$ei < _$i2; _$ei++) {
        _$l1 = _$nd["charCodeAt"](_$ei);
        if (_$l1 >= 40 && _$l1 < 126) _$pY[_$ei] = String.fromCharCode(_$l1 + 1);
        else if (_$l1 === 126) _$pY[_$ei] = '(';
        else _$pY[_$ei] = _$nd["charAt"](_$ei);
    }
    return _$pY.join('');
}
function _$vt() {
    var _$nd, _$i2 = [];
    for (var _$pY = 0; _$pY < 256; _$pY++) {
        _$nd = _$pY;
        for (var _$ei = 0; _$ei < 8; _$ei++) _$nd = ((_$nd & 1) ? (0xEDB88320 ^ (_$nd >>> 1)) : (_$nd >>> 1));
        _$i2[_$pY] = _$nd;
    }
    return _$i2;
}
function _$fs(_$nd, _$i2, _$pY, _$ei) {
    if (_$i2 == '=') return _$nd[_$pY] = _$ei;
    else if (_$i2 == "+=") return _$nd[_$pY] += _$ei;
}

function _$h5(_$nd, _$i2) {
    var _$pY = [],
        _$ei;
    for (_$ei = 0; _$ei < 2; _$ei++) _$pY.push(_$nd[_$ei] ^ _$i2[_$ei]);
    return _$pY;
}

function _$d9(_$nd, _$i2) { for (var _$pY = 0; _$pY < _$i2["length"]; _$pY++) _$nd.push(_$i2[_$pY]); }

function _$xC(_$nd) {++_$yu; }

// 返回时间戳
function _$ws() { return new Date()["getTime"](); }

function _$vd(_$nd, _$i2) {
    var _$pY = [];
    for (var _$ei = 2; _$ei < arguments["length"]; _$ei++) _$pY.push(arguments[_$ei]);
    if ("submit" == _$i2)
        if (_$sT(_$nd) && _$di(_$nd["tagName"], "form")) return _$nd[_$i2]["apply"](_$nd, _$pY);
        else if (_$pY["length"] === 0 && _$nd && _$nd["length"] == 1 && _$nd["jquery"] && _$sT(_$nd[0]) && _$qI(_$nd[0], "form")) return _$nd[_$i2]["apply"](_$nd, _$pY);
    else return _$xP(_$nd, _$i2, _$pY);
    return _$nd[_$i2]["apply"](_$nd, _$pY);
}

function _$uK(_$nd) { var _$i2 = []; for (var _$pY = 1; _$pY < arguments["length"]; _$pY++) _$i2.push(arguments[_$pY]); return _$nd["apply"](_$i2); }

function _$ey(_$nd) { return unescape(encodeURIComponent(_$nd)); }

function _$ro(_$nd, _$i2) {
    _$i2 = _$i2["split"](',');
    for (var _$pY = 0; _$pY < _$i2["length"]; _$pY++)
        if (_$nd[_$i2[_$pY]] !== _$u4) return 1;
}

function _$eJ(_$nd, _$i2) { if (typeof _$nd === "string") _$nd = _$jg(_$nd); var _$pY = new _$um(_$i2, true); return _$pY._$uw(_$nd, true); }

function _$lw(_$nd, _$i2) {
    _$nd = _$nd.split('`');
    _$i2 = _$lT(_$i2, 2);
    var _$pY = String.fromCharCode(95, 36);
    for (var _$ei = 0; _$ei < _$i2.length; _$ei++) _$i2[_$ei] = _$pY + _$i2[_$ei];
    var _$l1 = [String.fromCharCode(118, 97, 114, 32)];
    for (var _$ei = 0; _$ei < _$nd.length; _$ei++) {
        if (_$ei > 0) _$l1.push(',');
        _$l1.push(_$i2[_$ei] + '="' + _$nd[_$ei] + '"');
    }
    _$l1.push(';');
    return _$l1.join('');
}

function _$tt(_$nd) { _$nd = _$it(_$it(_$nd, '#')[0], '?')[0]; return _$nd["substr"](0, _$nd["lastIndexOf"]('/') + 1); }

function _$rY(_$nd, _$i2, _$pY) {
    _$i2 = _$i2 || 0;
    if (_$pY === _$u4) _$pY = _$nd.length;
    var _$ei = [],
        _$l1;
    while (true) {
        _$l1 = _$i2 + 40960;
        if (_$l1 >= _$pY) { _$ei.push(String.fromCharCode.apply(null, _$nd.slice(_$i2, _$pY))); break; } else {
            _$ei.push(String.fromCharCode.apply(null, _$nd.slice(_$i2, _$l1)));
            _$i2 = _$l1;
        }
    }
    return _$ei.join('');
}

function _$gi(_$nd, _$i2) {;
    _$i2 = _$xO(_$i2);
    var _$pY = Math["floor"](_$nd["length"] / 8),
        _$ei, _$l1 = [],
        _$ta = [],
        _$qm = 8 - (_$nd["length"] % 8),
        _$eB;
    _$eB = _$xO(_$e4(8));
    _$ta = _$eB["slice"](0);
    for (_$ei = 0; _$ei < _$pY; _$ei++) _$l1.push(_$xO(_$nd["slice"](_$ei * 8, _$ei * 8 + 8)));
    var _$lg = _$nd["slice"](_$pY * 8);
    for (_$ei = 0; _$ei < _$qm; _$ei++) _$lg.push(_$qm);
    _$l1.push(_$xO(_$lg));
    for (_$ei = 0; _$ei < _$l1["length"]; _$ei++) {
        _$iU(_$h5(_$l1[_$ei], _$eB), _$ta, _$i2);
        _$eB = _$ta["slice"](_$ta["length"] - 2);
    }
    var _$ff = [];
    _$bb(_$ta, _$ff);
    return _$ff;
}

function _$y3(_$nd) {
    var _$i2 = _$zT(_$nd),
        _$pY = (_$i2[0] << 8) + _$i2[1],
        _$ei = _$i2["length"],
        _$l1;
    for (_$l1 = 2; _$l1 < _$ei; _$l1 += 2) {
        _$i2[_$l1] ^= (_$pY >> 8) & 0xFF;
        if (_$l1 + 1 < _$ei) _$i2[_$l1 + 1] ^= _$pY & 0xFF;
        _$pY++;
    }
    return _$i2["slice"](2);
}

function _$wx() { if ("1" == _$vi(24)) window["setInterval"](_$bp, 2000); }

function _$pS(_$nd) { _$nd = window["Math"]["round"](_$nd); return [((_$nd & 0xFF00) >> 8), (_$nd & 0xFF)]; }

function _$wt() {;

    function _$nd(_$kc, _$bW, _$sK) { _$bW = _$bW["split"](','); for (var _$dE = 0; _$dE < _$bW["length"]; _$dE++) _$sK.push(_$kc[_$bW[_$dE]] || 0); }
    var _$i2 = [],
        _$pY, _$ei, _$l1;
    var _$ta = window["navigator"];
    for (_$pY in _$ta) { try { _$l1 = _$ta["hasOwnProperty"](_$pY); } catch (_$qm) { _$l1 = false; } if (_$l1) { _$i2.push(_$pY); if (_$pY !== "appVersion" && _$pY !== "userAgent") { _$ei = _$ta[_$pY]; if (typeof _$ei !== "object") _$i2.push(_$ei); } } }
    _$i2.push((_$ta["languages"] || []).join(','));
    var _$eB = _$ta["plugins"];
    if (_$eB)
        for (_$pY = 0; _$pY < _$eB["length"]; _$pY++) {
            _$ei = _$eB[_$pY];
            if (_$ei["name"]) _$i2.push(_$ei["name"]);
            else if (_$ei["filename"]) _$i2.push(_$ei["filename"]);
        }
    _$wa(_$i2);
    var _$lg = _$ta["mimeTypes"];
    if (_$lg)
        for (_$pY = 0; _$pY < _$lg["length"]; _$pY++) {
            _$ei = _$lg[_$pY];
            if (_$ei["type"]) _$i2.push(_$ei["type"]);
            else if (_$ei["description"]) _$i2.push(_$ei["description"]);
        }
    var _$ff = window["screen"];
    var _$xs = "width,height,pixelDepth,colorDepth";
    _$xs = _$xs["split"](',');
    for (_$pY = 0; _$pY < _$xs["length"]; _$pY++)
        if (typeof _$ff[_$xs[_$pY]] === "number") _$i2.push(_$ff[_$xs[_$pY]]);
    _$i2.push(new Date()["getTimezoneOffset"]());
    var _$vI = "safari,ontouchstart,sidebar,localStorage,clipboardData,sessionStorage,indexedDB,openDatabase,standalone,$PreUCBrowserClassic,UCBrowserMessageCenter,__firefox__,_firefox_ReaderMode,__mttCreateFrame,mttCustomJS,__crWeb,__gCrWeb,MicroMessenger,SogouMse,ucweb,qb_bridge,FaveIconJavaInterface,jesion,dophin,orientation";
    _$vI = _$vI["split"](',');
    for (_$pY = 0; _$pY < _$vI["length"]; _$pY++) _$i2.push(window[_$vI[_$pY]] !== _$u4 ? 1 : 0);
    _$ei = _$wC("$_f0", _$vb);
    if (_$ei) _$i2.push(_$ei);
    _$ei = _$wC("$_f1", _$sp);
    if (_$ei) _$i2.push(_$ei);
    _$ei = _$wC("$_fh0");
    if (_$ei) _$i2.push(_$ei);
    return _$jv(_$i2.join(':'));
}

function _$pf() {
    var _$nd = 0,
        _$i2 = "_Selenium_IDE_Recorder,_selenium,callSelenium",
        _$pY = "__driver_evaluate,__webdriver_evaluate,__selenium_evaluate,__fxdriver_evaluate,__driver_unwrapped,__webdriver_unwrapped,__selenium_unwrapped,__fxdriver_unwrapped,__webdriver_script_func,__webdriver_script_fn",
        _$ei = ["selenium", "webdriver", "driver"];
    try {
        _$nd = _$ro(window, _$i2) || _$ro(document, _$pY);
        for (var _$l1 in document)
            if (_$l1[0] === '$' && _$l1["match"]('^\\$[a-z]dc_') && document[_$l1]["cache_"]) _$nd = 1;
        for (var _$ta = 0; _$ta < _$ei["length"]; _$ta++)
            if (document["documentElement"]["getAttribute"](_$ei[_$ta])) _$nd = 1;
    } catch (_$qm) {; }
    if (_$nd) {
        window._$y1 = 1;
        _$oG(134217728, 31);
    }
}

function _$t3() {
    _$xS = "qrcklmDoExthWJiHAp1sVYKU3RFMQw8IGfPO92bvLNj.7zXBaSnu0TC6gy_4Ze5d";
    _$xS = _$xS["split"]('');
    _$wl = window["document"];
    _$b1 = top["location"];
    if (opener) _$jM = opener["location"];
    else _$jM = null;
    _$pP = window["Math"]["random"];
    _$us = window["setTimeout"];
    _$ue = window["setInterval"];
    _$zZ = window["$_ts"];
    localStorage = window["localStorage"];
    if (localStorage) try {
        localStorage["___ts___"] = "___ts___";
        localStorage["removeItem"]("___ts___");
        localStorage["__#classType"] = "localStorage";
    } catch (_$nd) { localStorage = _$u4; }
    if (!_$hT && !_$ps) {
        _$ps = 0;
        _$hT = 0;
        _$xg = 0;
    }
    window["console"] = window["console"] || (function() {
        var _$i2 = {};
        _$i2["log"] = function() {};
        return _$i2;
    })();
    if (!_$zZ) {
        _$zZ = new Object();
        window["$_ts"] = _$zZ;
    }
    _$uG = _$zT("wP3dxhyJgpbC6tVm_ewcCO");
}

function _$db(_$nd) {
    var _$i2 = Number(_$vi(23)) / 1000;
    var _$pY = _$d1() / 1000;
    if (!(_$vD & 64) || _$pY - _$i2 >= 60 || (_$ps & 134217728)) _$nd += "&T=" + _$wY(11);
    var _$ei = document["createElement"]("script");
    _$ei["setAttribute"]("src", "/4QbVtADbnLVIc/jW39ezbWPr.js?" + _$nd);
    document["body"]["appendChild"](_$ei);
    _$ei["onload"] = _$ei["onreadystatechange"] = function() {
        if (!this["readyState"] || this["readyState"] === "loaded" || this["readyState"] === "complete") {
            _$ei["parentNode"]["removeChild"](_$ei);
            _$ei["onload"] = _$ei["onreadystatechange"] = null;
        }
    };
}

function _$dN(_$nd) { return _$zE[_$nd["charCodeAt"](0)]; }

function _$c0(_$nd, _$i2) {
    _$nd = "FSSBB" + _$nd;
    if (typeof _$i2 === "object") _$i2 = _$zH(_$i2);
    _$i2 = _$iV(_$i2["toString"]());
    if (_$i2["length"] > 16 || _$i2["indexOf"](';') !== -1) _$i2 = _$zQ(_$oY(_$i2));
    if (localStorage) {
        var _$pY = parseInt(_$ws() / (1000 * 60 * 60));
        var _$ei = localStorage[_$nd];
        if (_$ei) { _$ei = _$it(_$ei, ':'); if (_$ei["length"] === 2 && _$ei[1] === _$i2 && _$pY - _$ei[0] < 24) {; return true; } }
        localStorage[_$nd] = _$pY + ':' + _$i2;
    }
}

function _$wZ(_$nd) { if (typeof _$nd === "string") _$nd = _$jg(_$nd); var _$i2 = _$ds(function() { return _$hs; }); var _$pY = window[_$i2] || (window[_$i2] = _$vt()); var _$ei = 0 ^ (-1); for (var _$l1 = 0; _$l1 < _$nd["length"]; _$l1++) _$ei = (_$ei >>> 8) ^ _$pY[(_$ei ^ _$nd[_$l1]) & 0xFF]; return (_$ei ^ (-1)) >>> 0; }

function _$wh(_$nd) {
    var _$i2 = window["Math"]["ceil"](window["Math"]["random"]() * 256);
    _$bb([_$c6()], _$nd);
    for (var _$pY = 0; _$pY < _$nd["length"]; _$pY++) _$nd[_$pY] ^= _$i2;
    _$nd.push(_$i2);
    return _$nd;
}

function _$pk() {
    var _$nd = window["navigator"];

    function _$pY(_$ei) {
        _$a8 = parseInt(_$ei["level"] * 100);
        _$bN = _$ei["charging"];
        if (_$ei["chargingTime"] === window["Infinity"]) _$vE = 0;
        else _$vE = parseInt(_$ei["chargingTime"]);
    }
    try {
        if (_$nd["battery"]) _$pY(_$nd["battery"]);
        else if (_$nd["getBattery"]) _$nd["getBattery"]()["then"](_$pY);
        else return;
    } catch (_$i2) {}
}

// 输出当前IE的版本号，Chrome返回undefined
function _$vB() {
    var _$nd = 3,
        _$i2 = document["createElement"]("div"),
        _$pY = _$i2["getElementsByTagName"]('i');
    while (_$i2["innerHTML"] = "<!--[if gt IE " + (++_$nd) + "]><i></i><![endif]-->", _$pY[0]);
    if (_$nd > 4) return _$nd;
    if (window["eval"]("/*@cc_on!@*/false")) return 10;
    try { if (new window["ActiveXObject"]("Microsoft.XMLHTTP") ? true : false) return 11; } catch (_$ei) {}
}

function _$it(_$nd, _$i2) { var _$pY = _$nd["indexOf"](_$i2); if (_$pY === -1) return [_$nd]; return [_$nd["substr"](0, _$pY), _$nd["substr"](_$pY + 1)]; }

function _$eK() {
    for (var _$nd in window)
        if (_$gK(_$nd, "WebXMLogMsg_UNIQUE_")) return 1;
}

function _$v9(_$nd) {
    _$yo++;
    _$oN = _$ws();
    _$xk(_$nd);
    _$dW(4);
}

function _$di(_$nd, _$i2) { return typeof _$nd == "string" && typeof _$i2 == "string" && _$nd["toLowerCase"]() === _$i2["toLowerCase"](); }

function _$aK(_$nd, _$i2) { if (_$nd) { _$nd = parseInt(_$nd); if (!window["isNaN"](_$nd)) return _$nd; } if (arguments["length"] > 1) return _$i2; return window["NaN"]; }

function _$aL(_$nd) {
    var _$i2 = "/",
        _$pY = 1,
        _$ei = "";
    var _$l1 = _$it(_$nd, "?");
    if (_$l1["length"] === 2) _$ei = _$l1[1];
    _$nd = _$l1[0];
    while (_$pY < _$nd["length"]) {
        if (_$nd["charAt"](_$pY) === "/") { _$pY++; continue; }
        var _$ta = _$pY;
        while (_$ta < _$nd["length"]) {
            if (_$nd["charAt"](_$ta) === "/") break;
            _$ta++;
        }
        if (_$nd["charAt"](_$pY) === ".") {
            if (_$ta - _$pY === 1) {} else if (_$ta - _$pY === 2 && _$nd["charAt"](_$pY + 1) === ".") {
                if (_$i2["length"] === 1) { _$pY = _$ta + 1; continue; }
                var _$qm = _$i2["length"] - 2;
                while (_$qm > 0 && _$i2["charAt"](_$qm) !== "/") _$qm--;
                _$i2 = _$i2["slice"](0, _$qm + 1);
            } else _$i2 += _$nd["slice"](_$pY, _$ta + 1);
        } else _$i2 += _$nd["slice"](_$pY, _$ta + 1);
        if (_$i2["charAt"](_$i2["length"] - 1) !== "/") _$i2 += "/";
        _$pY = _$ta + 1;
    }
    if (_$nd["charAt"](_$nd["length"] - 1) !== "/" && _$i2["length"] > 1) _$i2 = _$i2["slice"](0, _$i2["length"] - 1);
    if (_$ei["length"] > 0) _$i2 += "?" + _$ei;
    return _$i2;
}

function _$vb() {
    if (_$zG && _$zG <= 8) return _$u4;
    var _$nd = document["createElement"]("canvas");
    if (_$nd && _$nd["getContext"]) {
        _$nd["width"] = 200;
        _$nd["height"] = 50;
        var _$i2 = _$nd["getContext"]("2d");
        var _$pY = "ActiveXObject";
        _$i2["textBaseline"] = "top";
        _$i2["font"] = _$zN("Wsfa8cqvAUxN3Kav");
        _$i2["fillStyle"] = "#f82";
        _$i2["fillRect"](0, 0, 100, 30);
        _$i2["fillStyle"] = "#17e";
        _$i2["fillText"](_$pY, 3, 16);
        _$i2["fillStyle"] = "rgba(240,110,53,0.4)";
        _$i2["fillText"](_$pY, 5, 18);
        return _$zQ(_$jv(_$nd["toDataURL"]()));
    }
}

function _$vA(_$nd) {
    _$ye++;
    _$xk(_$nd);
}

function _$wb() {
    if (_$zG) {
        var _$nd = document["createElement"]("div");
        _$nd["innerHTML"] = _$zN("HDePFbYOwcrNRk0P3bEgWbzjEPrOMDmuQC29H1xOMoJNRkLuWkVaROGSi10yiDEThslS3C3z3bEgWP0aWDmfWkrPRDJ2WDEPEowNRopLH1EaQoGPEDf2FKwLwk0PWorgEOgZhCePFbYOwkg");
        document["body"]["appendChild"](_$nd);
        var _$i2 = document["getElementById"]("bb82kj");
        if (_$i2["fonts"]) {
            var _$pY = [];
            for (var _$ei = 1; _$ei < _$i2["fonts"]["Count"]; _$ei++) _$pY.push(_$i2["fonts"](_$ei));
            _$a9(_$pY.join(','));
        }
        document["body"]["removeChild"](_$nd);
    } else if (_$u9()) {
        var _$nd = document["createElement"]("div");
        _$nd["setAttribute"]("id", "3jeALeSsa6");
        _$nd["innerHTML"] = "<EMBED id=4rJFe6jNL52p height=1 type=application/x-shockwave-flash width=1 src=/4QbVtADbnLVIc/4rJFe6jNL52p.js>";
        document["body"]["appendChild"](_$nd);
        var _$l1 = 0;
        var _$ta = window["setInterval"](function() {
            try { var _$bW = _$wC("$_fh0"); if (!_$bW) { var _$sK = document["getElementById"]("4rJFe6jNL52p"); if (_$sK && typeof _$sK["GetVariable"] != "undefined") _$a9(_$sK["GetVariable"]("/:user_fonts")); } } catch (_$dE) {; }
            _$l1++;
            if (_$l1 > 50 || _$bW) { window["clearInterval"](_$ta); if (document["getElementById"]("3jeALeSsa6")) document["body"]["removeChild"](_$nd); }
        }, 100);
    } else {
        var _$qm;
        var _$eB;
        var _$lg = _$wC("$_fh0");
        if (_$lg) return;
        try {
            _$qm = new Array();
            _$eB = "DFPhelvetica;Tibetan Machine Uni;Cooljazz;Verdana;Helvetica Neue LT Pro 35 Thin;tahoma;LG Smart_H test Regular;DINPro-light;Helvetica LT 43 Light Extended;HelveM_India;SECRobotoLight Bold;OR Mohanty Unicode Regular;Droid Sans Thai;Kannada Sangam MN;DDC Uchen;clock2016_v1.1;SamsungKannadaRegular;MI LANTING Bold;SamsungSansNum3L Light;verdana;HelveticaNeueThin;SECFallback;SamsungEmoji;Telugu Sangam MN;Carrois Gothic SC;Flyme Light Roboto Light;SoMA-Digit Light;SoMC Sans Regular;HYXiYuanJ;sst;samsung-sans-num4T;gm_mengmeng;Lohit Kannada;times new roman;samsung-sans-num4L;serif-monospace;SamsungSansNum-3T Thin;ColorOSUI-XThin;Droid Naskh Shift Alt;SamsungTeluguRegular;Bengali OTS;MI LanTing_GB Outside YS;FZMiaoWu_GB18030;helve-neue-regular;SST Medium;Courier New;Khmer Mondulkiri Bold;Helvetica LT 23 Ultra Light Extended;Helvetica LT 25 Ultra Light;Roboto Medium;Droid Sans Bold;goudy;sans-serif-condensed-light;SFinder;noto-sans-cjk-medium;miui;MRocky PRC Bold;AndroidClock Regular;SamsungSansNum-4L Light;sans-serif-thin;AaPangYaer;casual;BN MohantyOT Bold;x-sst;NotoSansMyanmarZawgyi;Helvetica LT 33 Thin Extended;AshleyScriptMT Alt;Noto Sans Devanagari UI;Roboto Condensed Bold;Roboto Medium Italic;miuiex;Noto Sans Gurmukhi UI;SST Vietnamese Light;LG_Oriya;hycoffee;x-sst-ultralight;DFHeiAW7-A;FZZWXBTOT_Unicode;Devanagari Sangam MN Bold;sans-serif-monospace;Padauk Book Bold;LG-FZYingBiKaiShu-S15-V2.2;LG-FZYingBiKaiShu-S15-V2.3;HelveticaNeueLT Pro 35 Th;Microsoft Himalaya;SamsungSansFallback;SST Medium Italic;AndroidEmoji;SamsungSansNum-3R;ITC Stone Serif;sans-serif-smallcaps;x-sst-medium;LG_Sinhalese;Roboto Thin Italic;century-gothic;Clockopia;Luminous_Sans;Floridian Script Alt;Noto Sans Gurmukhi Bold;LTHYSZK Bold;GS_Thai;SamsungNeoNum_3T_2;Arabic;hans-sans-normal;Lohit Telugu;HYQiHei-50S Light;Lindsey for Samsung;AR Crystalhei DB;Samsung Sans Medium;samsung-sans-num45;hans-sans-bold;Luminous_Script;SST Condensed;SamsungDevanagariRegular;Anjal Malayalam MN;SamsungThai(test);FZLanTingHei-M-GB18030;Hebrew OTS;GS45_Arab(AndroidOS);Samsung Sans Light;Choco cooky;helve-neue-thin;PN MohantyOT Medium;LG-FZKaTong-M19-V2.4;Droid Serif;SamsungSinhalaRegular;helvetica;LG-FZKaTong-M19-V2.2;Noto Sans Devanagari UI Bold;SST Light;DFPEmoji;weatherfontnew Regular;RobotoNum3R;DINPro-medium;Samsung Sans Num55;SST Heavy Italic;LGlock4 Regular_0805;Georgia;noto-sans-cjk;Telugu Sangam MN Bold;MIUI EX Normal;HYQiHei-75S Bold;NotoSansMyanmarZawgyi Bold;yunospro-black;helve-neue-normal;Luminous_Serif;TM MohantyOT Normal;SamsungSansNum-3Lv Light;Samsung Sans Num45;SmartGothic Medium;georgia;casual-font-type;Samsung Sans Bold;small-capitals;MFinance PRC Bold;FZLanTingHei_GB18030;SamsungArmenian;Roboto Bold;century-gothic-bold;x-sst-heavy;SST Light Italic;TharLon;x-sst-light;Dinbol Regular;SamsungBengaliRegular;KN MohantyOTSmall Medium;hypure;SamsungTamilRegular;Malayalam Sangam MN;Noto Sans Kannada UI;helve-neue;Helvetica LT 55 Roman;Noto Sans Kannada Bold;Sanpya;SamsungPunjabiRegular;samsung-sans-num4Lv;LG_Kannada;Samsung Sans Regular;Zawgyi-One;Droid Serif Bold Italic;FZKATJW;courier new;SamsungEmojiRegular;MIUI EX Bold;Android Emoji;Noto Naskh Arabic UI;LCD Com;Futura Medium BT;Vivo-extract;Bangla Sangam MN Bold;hans-sans-regular;SNum-3R;SNum-3T;hans-sans;SST Ultra Light;Roboto Regular;Roboto Light;Hanuman;newlggothic;DFHeiAW5-A;hans-sans-light;Plate Gothic;SNum-3L;Helvetica LT 45 Light;Myanmar Sangam Zawgyi Bold;lg-sans-serif-light;MIUI EX Light;Roboto Thin;SoMA Bold;Padauk;Samsung Sans;Spacious_SmallCap;sans-serif;DV MohantyOT Medium;Stable_Slap;monaco;Flyme-Light;fzzys-dospy;ScreenSans;clock2016;Roboto Condensed Bold Italic;Arial;KN Mohanty Medium;MotoyaLMaru W3 mono;Handset Condensed;Roboto Italic;HTC Hand;SST Ultra Light Italic;SST Vietnamese Roman;Noto Naskh Arabic UI Bold;chnfzxh-medium;SNumCond-3T;century-gothic-regular;default_roboto-light;Noto Sans Myanmar;Myanmar Sangam MN;Apple Color Emoji;weatherfontReg;SamsungMalayalamRegular;arial;Droid Serif Bold;CPo3 PRC Bold;MI LANTING;SamsungKorean-Regular;test45 Regular;spirit_time;Devanagari Sangam MN;ScreenSerif;Roboto;cursive-font-type;STHeiti_vivo;chnfzxh;Samsung ClockFont 3A;Roboto Condensed Regular;samsung-neo-num3R;GJ MohantyOT Medium;Chulho Neue Lock;roboto-num3L;helve-neue-ultraLightextended;SamsungOriyaRegular;SamsungSansNum-4Lv Light;MYingHei_18030_C2-Bold;DFPShaoNvW5-GB;Roboto Black;helve-neue-ultralight;gm_xihei;LGlock4 Light_0805;Gujarati Sangam MN;Malayalam Sangam MN Bold;roboto-num3R;STXihei_vivo;FZZhunYuan_GB18030;noto-sans-cjk-light;coloros;Noto Sans Gurmukhi;Noto Sans Symbols;Roboto Light Italic;Lohit Tamil;cursive;default_roboto;BhashitaComplexSans Bold;LG_Number_Roboto Thin;monospaced-without-serifs;Helvetica LT 35 Thin;samsung-sans-num3LV;DINPro;Jomolhari;sans-serif-light;helve-neue-black;Lohit Bengali;Myanmar Sangam Zawgyi;Droid Serif Italic;Roboto Bold Italic;NanumGothic;Sony Mobile UD Gothic Regular;Georgia Bold Italic;samsung-sans-num3Lv;yunos-thin;samsung-neo-num3T-cond;Noto Sans Myanmar UI Bold;lgserif;FZYouHei-R-GB18030;Lohit Punjabi;baskerville;samsung-sans-num4Tv;samsung-sans-thin;LG Emoji;AnjaliNewLipi;SamsungSansNum-4T Thin;SamsungKorean-Bold;miuiex-light;Noto Sans Kannada;Roboto Normal Italic;Georgia Italic;sans-serif-medium;Smart Zawgyi;Roboto Condensed Italic;Noto Sans Kannada UI Bold;DFP Sc Sans Heue30_103;LG_Number_Roboto Bold;Padauk Book;x-sst-condensed;Sunshine-Uchen;Roboto Black Italic;Ringo Color Emoji;Devanagari OTS;Smart Zawgyi Pro;FZLanTingHei-M-GBK;AndroidClock-Large Regular;proportionally-spaced-without-serifs;Cutive Mono;times;LG Smart_H test Bold;DINPro-Light;sans-serif-black;Lohit Devanagari;proportionally-spaced-with-serifs;samsung-sans-num3L;MYoung PRC Medium;DFGothicPW5-BIG5HK-SONY;hans-sans-medium;SST Heavy;LG-FZZhunYuan-M02-V2.2;MyanmarUNew Regular;Noto Naskh Arabic Bold;SamsungGujarathiRegular;fantasy;helve-neue-light;Helvetica Neue OTS Bold;noto-sans-cjk-bold;samsung-sans-num3R;Lindsey Samsung;samsung-sans-num3T;ScreenSerifMono;ETrump Myanmar_ZW;helve-neue-thinextended;Noto Naskh Arabic;LG_Gujarati;Smart_Monospaced;Tamil Sangam MN;LG Emoji NonAME;Roboto Condensed Light Italic;gm_jingkai;FZLanTingKanHei_GB18030;lgtravel;palatino;Georgia Bold;Droid Sans;LG_Punjabi;SmartGothic Bold;Samsung Sans Thin;SST Condensed Bold;Comics_Narrow;courier;Oriya Sangam MN;helve-neue-lightextended;FZLanTingHei-R-GB18030;AR CrystalheiHKSCS DB;serif;RTWSYueRoudGoG0v1-Regular;MiaoWu_prev;FZY1K;LG_Number_Roboto Regular;AndroidClock;SoMA Regular;HYQiHei-40S Lightx;lg-sans-serif;Dancing Script Bold;default;sec-roboto-light;ColorOSUI-Regular;test Regular;Tamil Sangam MN Bold;FZYingBiXingShu-S16;RobotoNum3L Light;monospaced-with-serifs;samsung-sans-num35;Cool jazz;SamsungNeoNum-3L;STXingkai;ScreenSansMono;DFPWaWaW5-GB;SamsungSansNum-3L Light;Bangla Sangam MN;Gurmukhi Sangam MN;SECRobotoLight;hyfonxrain;MYingHeiGB18030C-Bold;samsung-sans-light;Helvetica LT 65 Medium;Droid Sans Fallback;Roboto Test1 Bold;Noto Sans Myanmar Bold;sans-serif-condensed-custom;SamsungNeoNum-3T;Samsung Sans Num35;monospace;TL Mohanty Medium;helve-neue-medium;LTHYSZK;Roboto Condensed custome Bold;Myanmar3;Droid Sans Devanagari;ShaoNv_prev;samsung-neo-num3L;FZLanTingHei-EL-GBK;yunos;samsung-neo-num3T;Times New Roman;helve-neue-bold;noto-sans-cjk-regular;Noto Sans Gurmukhi UI Bold;DINPro-black;FZLanTingHei-EL-GB18030;SST Vietnamese Medium;Roboto Condensed Light;SST Vietnamese Bold;AR DJ-KK;Droid Sans SEMC;Noto Sans Myanmar UI;Coming Soon;MYuppy PRC Medium;Rosemary;Lohit Gujarati;Roboto Condensed custom Bold;FZLanTingHeiS-R-GB;Helvetica Neue OTS;Kaiti_prev;Roboto-BigClock;FZYBKSJW;Handset Condensed Bold;SamsungGeorgian;Dancing Script;sans-serif-condensed;hans-sans-thin;SamsungSansNum-4Tv Thin;Lohit Odia;BhashitaComplexSans"["split"](';');
            var _$nd = document["createElement"]("div");
            _$nd["style"]["visibility"] = "hidden";
            _$nd["innerHTML"] = _$zN("HoJa3KgGQ6pyMDVeEbRBMvAzRbmzFKSyibTzMDSNFszbMCy0hUJN8bV_Wsl0QoGPHbTzMKTzMKTzMKTzMDSNFK9Zh6Ja3Kg5");
            document["body"]["appendChild"](_$nd);
            var _$ff = _$nd["children"][0];
            var _$xs = _$ff["offsetWidth"];
            var _$vI = _$ff["offsetHeight"];
            for (var _$ei = 0; _$ei < _$eB["length"]; ++_$ei) { _$ff["style"]["fontFamily"] = _$eB[_$ei]; if (_$xs != _$ff["offsetWidth"] || _$vI != _$ff["offsetHeight"]) _$qm.push(_$eB[_$ei]); }
            _$a9(_$qm.join(';'));
            document["body"]["removeChild"](_$nd);
        } catch (_$kc) {; }
    }
}

function _$uF(_$nd) { if (_$zZ._$cL) _$nd[14] = _$zZ._$cL - _$zZ._$bG; }

function _$q5() {
    if (!_$gK(_$bJ()["href"], "http")) {;
        var _$nd = document["createElement"]("script");
        _$nd["setAttribute"]("src", "http://security.riversecurity.com/4QbVtADbnLVIc/jW39ezbWPr.js");
        document["body"]["appendChild"](_$nd);
        _$sJ();
    }
}

function _$iP(_$nd, _$i2, _$pY) { return _$pY; }

function _$lS(_$nd) { _$nd = _$nd["split"]('.'); var _$i2 = window; for (var _$pY = 0; _$pY < _$nd["length"]; _$pY++) _$i2 = _$i2[_$nd[_$pY]]; return _$i2; }

function _$bC(_$nd) {
    _$s8(65536);
    _$yN++;
    if (typeof _$nd === "string") _$ir = [arguments[0], arguments[1], arguments[2]];
    else _$ir = [_$nd["message"], _$nd["filename"], _$nd["lineno"]];
}

function _$sL(_$nd) {
    _$nd = _$nd["trim"]();
    _$nd = _$s9(_$nd, '#');
    var _$i2 = _$nd[1];
    _$nd = _$nd[0];
    var _$pY = {};
    _$pY._$zD = _$i2;
    for (var _$ei in _$qs)
        if (_$qs["hasOwnProperty"](_$ei)) _$nd = _$nd["replace"](_$ei, _$qs[_$ei]);
    if (!(_$gK(_$nd["toLowerCase"](), "http://") || _$gK(_$nd["toLowerCase"](), "https://") || _$gK(_$nd, "//"))) {
        _$pY._$xY = 1;
        _$pY._$xX = _$nd;
        _$pY._$zj = "";
        _$pY._$jJ = _$bJ()["protocol"];
        return _$pY;
    }
    var _$l1 = document["createElement"]('a');
    _$l1["href"] = _$nd;
    for (var _$ei in _$tQ)
        if (_$tQ["hasOwnProperty"](_$ei)) _$l1["host"] = _$l1["host"]["replace"](_$ei, _$tQ[_$ei]);
    var _$ta = _$l1["protocol"];
    if (_$gK(_$nd, "//")) _$ta = _$bJ()["protocol"];
    var _$qm = _$l1["port"];
    if (_$qm === "")
        if (_$ta["toLowerCase"]() === "http:") _$qm = "80";
        else if (_$ta["toLowerCase"]() === "https:") _$qm = "443";
    var _$eB = ";" + _$l1["hostname"]["toLowerCase"]() + ":" + _$qm + ";";
    var _$lg = _$bJ()["protocol"];
    var _$ff = _$bJ()["port"];
    if (_$ff === "")
        if (_$lg["toLowerCase"]() === "http:") _$ff = "80";
        else if (_$lg["toLowerCase"]() === "https:") _$ff = "443";
    var _$xs = ";" + _$bJ()["hostname"]["toLowerCase"]() + ":" + _$ff + ";";
    if ((_$eB === _$xs) || (_$xF["indexOf"](_$eB) >= 0)) _$pY._$xY = 2;
    else _$pY._$xY = 3;
    if ((_$ta["toLowerCase"]() === "http:" && _$qm == "80") || (_$ta["toLowerCase"]() === "https:" && _$qm == "443")) _$pY._$zj = _$ta + "//" + _$l1["hostname"];
    else _$pY._$zj = _$ta + "//" + _$l1["host"];
    if (_$gK(_$l1["pathname"], '/')) _$pY._$xX = _$l1["pathname"] + _$l1["search"];
    else _$pY._$xX = '/' + _$l1["pathname"] + _$l1["search"];
    _$pY._$jJ = _$ta;
    return _$pY;
}

//返回网页编码，这里返回的是"GBK-"
function _$vM() {
    var _$nd = document["characterSet"] || document["charset"];
    if (_$nd && _$nd["toLowerCase"]() !== "utf-8" && _$nd["toLowerCase"]() != "windows-1252") _$nd += '-';
    else _$nd = '';
    return _$nd;
}

function _$aN(_$nd) {
    if (_$eH != _$nd["alpha"] || _$gq != _$nd["beta"] || _$xv != _$nd["gamma"]) {
        _$eH = _$nd["alpha"];
        _$gq = _$nd["beta"];
        _$xv = _$nd["gamma"];
        ++_$t1;
    }
}

function _$sT(_$nd) {
    if (typeof window["HTMLElement"] === "object") return _$nd instanceof window["HTMLElement"] || (_$nd !== null && _$nd["tagName"] != null && _$qI(_$nd, "iframe"));
    else return _$nd && typeof _$nd === "object" && _$nd !== null && ((_$nd["nodeType"] === 1 && typeof _$nd["nodeName"] === "string") || (_$nd["nodeType"] === 11 && typeof _$nd["nodeName"] === "document-fragment"));
}

// 返回消耗的时间，开始时间是调用 t0()的时候，结束时间是调用本函数的时候。
function _$d1() { return _$vC + _$ws() - _$vN; }

//Key function
function _$wv() {
    _$qY();
    var _$nd = window["ActiveXObject"];
    if (_$nd) window["ActiveXObject"] = function(_$ei, _$l1) {
        if (_$ei === "Microsoft.XMLHTTP") return _$vT(new _$nd(_$ei), false);
        else { if (_$l1) return new _$nd(_$ei, _$l1); return new _$nd(_$ei); }
    };
    var _$i2 = window["XMLHttpRequest"];
    if (_$i2) {
        var _$pY = _$i2["prototype"];
        if (_$pY) {
            _$jm = _$pY["open"];
            _$hf = _$pY["send"];
            _$pY["open"] = function() { arguments[1] = _$v8(arguments[1]); return _$jm["apply"](this, arguments); };
        } else window["XMLHttpRequest"] = function() { return _$vT(new _$i2(), false); };
    }
    if (window["Request"]) {
        _$fz = window["Request"];
        window["Request"] = function(_$ei, _$l1) {
            _$ei = _$v8(_$ei);
            if (_$l1) _$l1["credentials"] = "include";
            else _$l1 = { 'credentials': "include" };
            return new _$fz(_$ei, _$l1);
        };
    }
    if (window["fetch"]) {
        _$wF = window["fetch"];
        window["fetch"] = function() {
            if (typeof arguments[0] === "string") {
                arguments[0] = _$v8(arguments[0]);
                if (arguments[1]) arguments[1]["credentials"] = "include";
                else arguments[1] = { 'credentials': "include" };
            }
            return _$wF["apply"](this, arguments);
        };
    }
}

function _$wW(_$nd) {
    var _$i2;
    var _$pY = _$ws();
    if (_$xu > 0) {
        _$i2 = _$pY - _$xu;
        if (_$i2 < 60 * 1000) {
            _$yG += (_$pY - _$xu);
            _$uX = parseInt(_$yG / (++_$er));
        }
    }
    _$xu = _$pY;
    if (_$yn["length"] < 1100) _$yn.push(_$nd["keyCode"]);
    _$xW++;
    var _$ei = _$nd["keyCode"];
    if (_$ei === 32 || _$ei === 13) _$dW(5);
}

function _$fo(_$nd) { var _$i2 = arguments; return _$nd["replace"](/\{(.+?)\}/g, function(_$pY, _$ei) { return _$i2[parseInt(_$ei) + 1]; }); }

function _$iU(_$nd, _$i2, _$pY) {
    var _$ei = _$nd[0],
        _$l1 = _$nd[1],
        _$ta = 0,
        _$qm = 0x9E3779B9;
    for (var _$eB = 0; _$eB < 32; _$eB++) {
        _$ei = (_$ei + ((_$l1 << 4 ^ ((_$l1 >> 5) & 0x07ffffff)) + _$l1 ^ _$ta + _$pY[(_$ta & 3)])) & 0xffffffff;
        _$ta = (_$ta + _$qm) & 0xffffffff;
        _$l1 = (_$l1 + ((_$ei << 4 ^ ((_$ei >> 5) & 0x07ffffff)) + _$ei ^ _$ta + _$pY[(((_$ta >> 11) & 0x001fffff) & 3)])) & 0xffffffff;
    }
    _$i2.push(_$ei, _$l1);
}

function _$xj() {
    try {
        var _$nd = "hidden";
        if (_$nd in document) document["addEventListener"]("visibilitychange", _$i2);
        else if ((_$nd = "mozHidden") in document) document["addEventListener"]("mozvisibilitychange", _$i2);
        else if ((_$nd = "webkitHidden") in document) document["addEventListener"]("webkitvisibilitychange", _$i2);
        else if ((_$nd = "msHidden") in document) document["addEventListener"]("msvisibilitychange", _$i2);
        else return;
        _$rs = 0;
        if (document[_$nd] !== _$u4) _$i2();
    } catch (_$pY) {; }

    function _$i2() {
        var _$ei = !document[_$nd];
        if (_$ei == _$uf) return;
        _$uf = _$ei;
        if (_$uf) {;
            _$eT = _$ws();
        } else {;
            _$rs += _$ws() - _$eT;
        }
    }
}

function _$zP(_$nd) { return _$uW(_$y3(_$nd), _$aZ(2, _$xp(9))); }

function _$zN(_$nd) { var _$i2 = _$zT(_$nd); return _$uW(_$i2); }

function _$wd(_$nd, _$i2) {
    if (!localStorage) return;
    if (typeof _$nd === "number") _$nd = String(_$nd);
    var _$pY = _$tz(_$nd);
    if (_$pY) _$i2 = parseInt(_$pY) + _$i2;
    _$nd = "FSSBA" + _$zQ(_$nd);
    localStorage[_$nd] = _$i2;
}

function _$rv() {
    try {
        var _$nd = { '0.0.0.0': true, '127.0.0.1': true };
        var _$i2 = window["RTCPeerConnection"] || window["mozRTCPeerConnection"] || window["webkitRTCPeerConnection"];
        var _$pY = new RegExp('([0-9]{1,3}(\\.[0-9]{1,3}){3}|[a-f0-9]{1,4}(:[a-f0-9]{1,4}){7})');
        var _$ei = 0;
        try { _$ei = parseInt(_$zN(_$wC("$_vJTp"))); } catch (_$l1) {; }
        if (!_$i2) {; return; }
        var _$ta = _$ws();
        if (Math["abs"](_$ta - _$ei) < 300000) return;
        _$vs("$_vJTp", _$zQ(_$ta["toString"]()));
        var _$qm = JSON["parse"](_$zN("8nxBQopNMCyfMcEGiPrMEo7PVvpapDm03VJL3KyXRKSuEPq_EopnwKYeEmTe"));
        var _$eB = JSON["parse"]('{             \"iceServers\" : [                 {"url" : "stun:stun01.sipphone.com"}, {"url" : "stun:stun.ekiga.net"},                 {"url" : "stun:stun.fwdnet.net"}, {"url" : "stun:stun.ideasip.com"},                 {"url" : "stun:stun.iptel.org"}, {"url" : "stun:stun.rixtelecom.se"},                 {"url" : "stun:stun.schlund.de"}, {"url" : "stun:stun.l.google.com:19302"},                 {"url" : "stun:stun1.l.google.com:19302"}, {"url" : "stun:stun2.l.google.com:19302"},                 {"url" : "stun:stun3.l.google.com:19302"}, {"url" : "stun:stun4.l.google.com:19302"}             ]         }');
        var _$lg = new _$i2(_$eB, _$qm);
        _$lg["onicecandidate"] = function(_$dE) { if (_$dE["candidate"]) _$bW(_$dE["candidate"]["candidate"]); };
        _$lg["createDataChannel"]("");
        _$lg["createOffer"](function(_$dE) { _$lg["setLocalDescription"](_$dE, function() {}, function() {}); }, function() {});
        var _$ff = 0;
        var _$xs, _$vI;
        _$kc();
    } catch (_$l1) {; }

    function _$bW(_$dE) {
        var _$f3 = _$pY["exec"](_$dE),
            _$nI = _$f3 ? _$f3[1] : null;
        if (!_$nI || _$nd[_$nI]) return;
        _$nd[_$nI] = true;
        if (_$dE["indexOf"](" srflx ") !== -1) {
            _$vI = _$sK(_$nI);
            _$vs("$_JQnh", _$zQ(_$vI));
        } else if (_$dE["indexOf"](" host ") !== -1) {
            _$xs = _$sK(_$nI);
            _$vs("$_vvCI", _$zQ(_$xs));
        }
    }

    function _$sK(_$dE) {
        _$dE = _$dE["split"]('.');
        _$dE[0] = parseInt(_$dE[0]);
        _$dE[1] = parseInt(_$dE[1]);
        _$dE[2] = parseInt(_$dE[2]);
        _$dE[3] = parseInt(_$dE[3]);
        return _$dE;
    }

    function _$kc() {
        _$us(function() {
            var _$dE = _$lg["localDescription"]["sdp"]["split"]('\n');
            _$dE["forEach"](function(_$f3) { if (_$f3["indexOf"]("a=candidate:") === 0) _$bW(_$f3); });
            if (_$ff < 100 && !(_$xs && _$vI)) {
                _$kc();
                _$ff++;
            }
        }, 20);
    }
}

function _$sy(_$nd) { var _$i2 = _$tG(_$hn()); var _$pY = _$oY(_$i2)["slice"](0, 8); var _$ei = _$nd["indexOf"]('-'); if (_$ei != -1) _$nd = _$nd["substr"](_$ei + 1); var _$l1 = _$uc(_$nd); for (var _$ta = 0; _$ta < 8; _$ta++) _$pY[_$ta] ^= _$l1; return _$zQ(_$pY); }

function _$w4() { this._$yq(); }

function _$tG(_$nd) {
    var _$i2 = _$nd["slice"](0);
    if (_$i2["length"] < 5) return;
    var _$pY = _$i2["pop"]();
    var _$ei = 0;
    for (_$ei = 0; _$ei < _$i2["length"]; _$ei++) _$i2[_$ei] ^= _$pY;
    var _$l1 = _$i2["length"] - 4;
    var _$ta = _$c6() - _$xO(_$i2["slice"](_$l1))[0];
    _$i2 = _$i2["slice"](0, _$l1);
    var _$qm = window["Math"]["floor"](window["Math"]["log"](_$ta / 1.164 + 1));
    var _$eB = _$i2["length"];
    var _$lg = [0, _$m8][_$r3];
    for (_$ei = 0; _$ei < _$eB; _$ei++) _$i2[_$ei] = _$qm | (_$i2[_$ei] ^ _$lg);
    _$aZ(8, _$qm);
    return _$i2;
}

function _$cW(_$nd) { _$oG(0, _$nd); }

function _$jg(_$nd) {
    var _$i2 = [],
        _$pY;
    _$nd = _$ey(_$nd);
    for (_$pY = 0; _$pY < _$nd["length"]; _$pY++) _$i2.push(_$nd["charCodeAt"](_$pY));
    return _$i2;
}

function _$t0() {
    _$zG = _$vB(); //确定IE版本号,Chrome返回undefined。
    if (!String["prototype"]["trim"]) String["prototype"]["trim"] = _$ug;
    _$vW = _$vM(); "GBK-"
    _$gb(); // 确定 _$vf=[一个数组]，和网页中的一个元素（）有关，把两个字符串变为整数。
    _$hm(); 
}

function _$ui() {
    var _$nd = document["getElementsByTagName"]("script");
    for (i = _$nd["length"] - 1; i >= 0; i--)
        if (_$nd[i]["getAttribute"]('r') == 'm') _$nd[i]["parentElement"]["removeChild"](_$nd[i]);
}

function _$bp() { _$wB = window["eval"]("var a = new Date(); debugger; new Date() - a > 100;"); }

function _$qP(_$nd) {
    _$nd = _$nd + '=';
    var _$i2 = document["cookie"]["split"]("; "),
        _$pY, _$ei;
    for (_$pY = 0; _$pY < _$i2["length"]; _$pY++) { _$ei = _$i2[_$pY]; if (_$gK(_$ei, _$nd)) return _$ei["substr"](_$nd["length"]); }
}

function _$wC(_$nd, _$i2) {
    var _$pY = localStorage || _$zZ;
    var _$ei = _$pY[_$nd];
    if (!_$ei && _$i2 !== _$u4) {
        if (typeof _$i2 === "function") _$ei = _$i2();
        else _$ei = _$i2;
        if (_$ei) _$pY[_$nd] = _$ei;
    }
    return _$ei;
}

function _$jS(_$nd, _$i2) { return _$i2; }

function _$xT(_$nd) { return _$nS(_$nd, _$ly()); }

function _$tz(_$nd) {
    if (!localStorage) return;
    if (typeof _$nd === "number") _$nd = String(_$nd);
    _$nd = "FSSBA" + _$zQ(_$nd);
    return localStorage[_$nd];
}

function _$lT(_$nd, _$i2) {
    var _$pY = _$nd.length,
        _$ei = new Array(Math.ceil(_$nd.length / _$i2)),
        _$l1 = 0,
        _$ta = 0;
    for (; _$ta < _$pY; _$ta += _$i2, _$l1++) _$ei[_$l1] = _$nd.substr(_$ta, _$i2);
    return _$ei;
}

function _$uW(_$nd) {
    var _$i2 = [],
        _$pY, _$ei, _$l1, _$ta = '?' ["charCodeAt"](0);
    for (_$pY = 0; _$pY < _$nd["length"];) {
        _$ei = _$nd[_$pY];
        if (_$ei < 0x80) _$l1 = _$ei;
        else if (_$ei < 0xc0) _$l1 = _$ta;
        else if (_$ei < 0xe0) {
            _$l1 = ((_$ei & 0x3F) << 6) | (_$nd[_$pY + 1] & 0x3F);
            _$pY++;
        } else if (_$ei < 0xf0) {
            _$l1 = ((_$ei & 0x0F) << 12) | ((_$nd[_$pY + 1] & 0x3F) << 6) | (_$nd[_$pY + 2] & 0x3F);
            _$pY += 2;
        } else if (_$ei < 0xf8) {
            _$l1 = _$ta;
            _$pY += 3;
        } else if (_$ei < 0xfc) {
            _$l1 = _$ta;
            _$pY += 4;
        } else if (_$ei < 0xfe) {
            _$l1 = _$ta;
            _$pY += 5;
        } else _$l1 = _$ta;
        _$pY++;
        _$i2.push(_$l1);
    }
    return _$rY(_$i2);
}

function _$aH(_$nd) {
    if (_$op > 0) {
        _$yp += (_$ws() - _$op);
        ++_$yv;
        _$yx = parseInt(_$yp / _$yv);
        _$op = 0;
        _$dW(3);
    }
}

function _$fN(_$nd) { var _$i2 = _$vi(14); if (_$i2["length"] === 0) _$i2 = _$bJ()["protocol"] === "https:" ? "443" : _$i2 = "80"; return _$yU + _$i2 + _$nd; }

function _$zT(_$nd) {
    var _$i2 = _$nd["length"],
        _$pY = new Array(Math["floor"](_$i2 * 3 / 4));
    var _$ei, _$l1, _$ta, _$qm;
    var _$eB = 0,
        _$lg = 0,
        _$ff = _$i2 - 3;
    for (_$eB = 0; _$eB < _$ff; _$eB = _$eB + 4) {
        _$ei = _$zE[_$nd["charCodeAt"](_$eB)];
        _$l1 = _$zE[_$nd["charCodeAt"](_$eB + 1)];
        _$ta = _$zE[_$nd["charCodeAt"](_$eB + 2)];
        _$qm = _$zE[_$nd["charCodeAt"](_$eB + 3)];
        _$pY[_$lg++] = (_$ei << 2) | (_$l1 >> 4);
        _$pY[_$lg++] = ((_$l1 & 15) << 4) | (_$ta >> 2);
        _$pY[_$lg++] = ((_$ta & 3) << 6) | _$qm;
    }
    if (_$eB < _$i2) {
        _$ei = _$zE[_$nd["charCodeAt"](_$eB)];
        _$l1 = _$zE[_$nd["charCodeAt"](_$eB + 1)];
        _$pY[_$lg++] = (_$ei << 2) | (_$l1 >> 4);
        if (_$eB + 2 < _$i2) {
            _$ta = _$zE[_$nd["charCodeAt"](_$eB + 2)];
            _$pY[_$lg++] = ((_$l1 & 15) << 4) | (_$ta >> 2);
        }
    }
    return _$pY;
}

function _$bb(_$nd, _$i2) {
    for (var _$pY = 0; _$pY < _$nd["length"]; _$pY++) {
        var _$ei = _$nd[_$pY];
        _$i2.push((_$ei >>> 24) & 0xFF);
        _$i2.push((_$ei >>> 16) & 0xFF);
        _$i2.push((_$ei >>> 8) & 0xFF);
        _$i2.push(_$ei & 0xFF);
    }
}

function _$v1(_$nd, _$i2) {
    if (window._$xG) return;
    if (_$i2 !== _$u4 && !_$i2) return;
    console["log"](_$nd);
}

function _$q0(_$nd) { if (_$nd < 0xE0) return _$nd; return parseInt(Math["log"](_$nd) / Math["log"](2) + 0.5) | 0xE0; }

function _$ox(_$nd) { return Math["floor"](_$pP() * _$nd); }

function _$vK(_$nd) { return _$nd["cookie"]; }

function _$tK(_$nd, _$i2) {
    if (!_$nd) {
        if (localStorage && localStorage.$d === '1') debugger;
        if (_$i2) throw _$i2;
        else throw "assert failed with condition: " + _$nd;
    }
}

function _$ah() {
    var _$nd = _$wC("$_fr");

    function _$ei(_$l1) {
        try {
            var _$ta, _$qm = 0;
            for (var _$eB = 0; _$eB < _$l1["length"]; _$eB++) {
                var _$lg = _$l1[_$eB];
                var _$ff = _$lg["deviceId"] || _$lg.id;
                if (_$ff["length"] > 20) {
                    var _$xs = _$zQ(_$jv(_$ff));
                    _$ta = _$ta || _$xs;
                    if (_$nd === _$xs) _$qm = 1;
                }
            }
            if ((!_$qm || !_$nd) && _$ta) {
                _$nd = _$ta;
                _$vs("$_fr", _$nd);
            }
        } catch (_$vI) {; }
    }
    try { if (window["MediaStreamTrack"] && window["MediaStreamTrack"]["getSources"]) window["MediaStreamTrack"]["getSources"](function(_$l1) { _$ei(_$l1); }); var _$i2 = window["navigator"]; if (_$i2["mediaDevices"] && _$i2["mediaDevices"]["enumerateDevices"]) _$i2["mediaDevices"]["enumerateDevices"]()["then"](function(_$l1) { _$ei(_$l1); }); } catch (_$pY) {; }
    return _$nd;
}

function _$dW(_$nd) { var _$i2 = _$wY(_$nd); if (_$i2 && _$i2 !== _$u4) document["cookie"] = _$fN(_$zy) + '=' + _$i2 + "; path=/" + _$wL(365 * 10); }

function _$xO(_$nd) {; var _$i2 = []; for (var _$pY = 0; _$pY < _$nd["length"]; _$pY += 4) _$i2.push((_$nd[_$pY] << 24) | (_$nd[_$pY + 1] << 16) | (_$nd[_$pY + 2] << 8) | _$nd[_$pY + 3]); return _$i2; }

function _$iW(_$nd, _$i2) { var _$pY = _$zT(_$nd); var _$ei = new _$um(_$i2); return _$ei._$yI(_$pY, true); }

function _$e4(_$nd) {
    var _$i2 = [],
        _$pY;
    for (_$pY = 0; _$pY < _$nd; _$pY++) _$i2.push(_$ox(256));
    return _$i2;
}

function _$uz(_$nd) {++_$wn; }

function _$um(_$nd) {
    if (!this._$yE[0][0][0]) this._$y5();
    var _$i2 = _$nd;
    if (_$nd["length"] % 16 != 0) _$i2 = _$tG(_$nd);
    var _$pY = _$xO(_$i2);
    var _$ei, _$l1, _$ta, _$qm, _$eB, _$lg = this._$yE[0][4],
        _$ff = this._$yE[1],
        _$xs = _$pY["length"],
        _$vI = 1;
    this._$zf = [_$qm = _$pY["slice"](0), _$eB = []];
    for (_$ei = _$xs; _$ei < 4 * _$xs + 28; _$ei++) {
        _$ta = _$qm[_$ei - 1];
        if (_$ei % _$xs === 0 || (_$xs === 8 && _$ei % _$xs === 4)) {
            _$ta = _$lg[_$ta >>> 24] << 24 ^ _$lg[_$ta >> 16 & 255] << 16 ^ _$lg[_$ta >> 8 & 255] << 8 ^ _$lg[_$ta & 255];
            if (_$ei % _$xs === 0) {
                _$ta = _$ta << 8 ^ _$ta >>> 24 ^ _$vI << 24;
                _$vI = _$vI << 1 ^ (_$vI >> 7) * 283;
            }
        }
        _$qm[_$ei] = _$qm[_$ei - _$xs] ^ _$ta;
    }
    for (_$l1 = 0; _$ei; _$l1++, _$ei--) {
        _$ta = _$qm[_$l1 & 3 ? _$ei : _$ei - 4];
        if (_$ei <= 4 || _$l1 < 4) _$eB[_$l1] = _$ta;
        else _$eB[_$l1] = _$ff[0][_$lg[_$ta >>> 24]] ^ _$ff[1][_$lg[_$ta >> 16 & 255]] ^ _$ff[2][_$lg[_$ta >> 8 & 255]] ^ _$ff[3][_$lg[_$ta & 255]];
    }
}

function _$zQ(_$nd, _$i2) {
    if (typeof _$nd === "string") _$nd = _$jg(_$nd);
    if (!_$i2) _$i2 = _$xS;
    var _$pY = '',
        _$ei;
    for (_$ei = 0; _$ei < _$nd["length"]; _$ei = _$ei + 3) {
        _$pY += _$i2[_$nd[_$ei] >> 2];
        _$pY += _$i2[((_$nd[_$ei] & 3) << 4) | (_$nd[_$ei + 1] >> 4)];
        if (_$nd[_$ei + 1] !== _$u4) _$pY += _$i2[((_$nd[_$ei + 1] & 15) << 2) | (_$nd[_$ei + 2] >> 6)];
        else {}
        if (_$nd[_$ei + 2] !== _$u4) _$pY += _$i2[_$nd[_$ei + 2] & 63];
    }
    return _$pY;
}

function _$vv() { var _$nd = 'ef ghi  jklmnoL U3F9\\_XM?Ep  q rs1PW\');A0@.7I<JDC=:RV85-O6]t uv[ QG#`^BY,/K$%&S(2!"4+TH>*ZNacbd'; for (var _$i2 = 0; _$i2 < 32; _$i2++) _$zE[_$i2] = 0; for (_$i2 = 0; _$i2 < _$nd.length; _$i2++) _$zE[_$i2 + 32] = _$nd.charCodeAt(_$i2) - 33; }

function _$xk(_$nd) {
    if (_$yn["length"] < 1100)
        for (var _$i2 = 0; _$i2 < _$nd["touches"]["length"]; _$i2++) {
            var _$pY = _$nd["touches"][_$i2];
            _$yn.push(_$pY["screenX"], _$pY["screenY"], _$pY["clientX"], _$pY["clientY"]);
        }
    _$dW(4);
}

function _$xP(_$nd, _$i2, _$pY) {
    switch (_$pY["length"]) {
        case 0:
            return _$nd[_$i2]();
        case 1:
            return _$nd[_$i2](_$pY[0]);
        case 2:
            return _$nd[_$i2](_$pY[0], _$pY[1]);
        case 3:
            return _$nd[_$i2](_$pY[0], _$pY[1], _$pY[2]);
        default:
            return _$vy(_$nd, _$i2, _$pY);
    }
}

function _$dr() {
    var _$nd = {},
        _$i2;
    var _$pY = window["eval"];
    var _$ei = _$uM(12);
    var _$l1 = _$ei["split"]('`');
    for (var _$ta = 0; _$ta < _$l1["length"]; _$ta++) {
        var _$qm = _$l1[_$ta];
        _$qm = _$qm["split"](':');
        try {
            var _$eB = parseInt(_$qm[0]);
            if (_$eB === 1) { _$i2 = _$lS(_$qm[2]); if (_$i2 === _$u4) continue; } else if (_$eB === 2) _$i2 = _$lS(_$qm[2]) !== _$u4 ? 1 : 0;
            else if (_$eB === 3) {
                _$i2 = _$pY(_$qm[2]);
                if (_$i2 === true) _$i2 = 1;
                else if (_$i2 === false) _$i2 = 0;
            } else;
        } catch (_$lg) {
            if (_$eB === 2) _$i2 = 0;
            else { _$i2 = "except"; }
        }
        _$nd[_$qm[1]] = _$i2;
    }
    _$i2 = _$wC("$_f0", _$vb);
    if (_$i2) _$nd[2] = _$i2;
    _$i2 = _$wC("$_f1", _$sp);
    if (_$i2) _$nd[18] = _$i2;
    _$nd[3] = _$zQ(_$wt());
    if (_$yN > 0) {
        _$nd[15] = _$yN;
        _$nd[16] = JSON["stringify"](_$ir);
    }
    _$i2 = _$wC("$_fh0");
    if (_$i2) _$nd[17] = _$i2;
    _$uF(_$nd);
    _$r1(_$nd);
    var _$ff = {},
        _$xs = 0;
    for (var _$vI in _$nd)
        if (_$nd["hasOwnProperty"](_$vI)) {
            _$i2 = _$nd[_$vI];
            if (!_$c0(_$vI, _$i2)) {
                _$ff[_$vI] = _$i2;
                _$xs = 1;
            }
        }
    if (_$xs) {
        _$ff[0] = _$uM(8);
        var _$kc = _$zH(_$ff);
        var _$bW = _$zQ(_$oY(_$kc));
        _$kc = _$bW + '=' + _$ud(_$kc, _$uG);
        _$us(function() { _$db(_$kc); }, 10);
    }
    _$s8(1024);
}

function _$xe(_$nd) {
    var _$i2 = _$nd["acceleration"] || _$nd["accelerationIncludingGravity"];
    if (_$yH != _$i2.x || _$tp != _$i2.y || _$w3 != _$i2.z) {
        _$yH = _$i2.x;
        _$tp = _$i2.y;
        _$w3 = _$i2.z;
        ++_$xD;
    }
}
'''

r = execjs.eval(js_a)
print(r)
