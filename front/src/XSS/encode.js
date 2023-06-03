function encodeForHTMLAttibute(str) {
  let hex
  let encoded = ''
  for (let i = 0; i < str.length; i++) {
    let ch = hex = str[i]
    if (!/[A-Za-z0-9]/.test(str[i]) && str.charCodeAt(i) < 256) {
      hex = '&#x' + ch.charCodeAt(0).toString(16) + ';'
    }
    encoded += hex
  }
  return encoded
}
function encodeForHTML(str) {
  return ('' + str)
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')     // DEC=> &#60; HEX=> &#x3c; Entity=> &lt;
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&#x27;')   // &apos; 不推荐，因为它不在HTML规范中
    .replace(/\//g, '&#x2F;');

}
function encodeForJavascript(str) {
  let hex;
  let encoded = ''
  for (let i = 0; i < str.length; i++) {
    let cc = hex = str[i];
    if (!/[A-Za-z0-9]/.test(str[i]) && str.charCodeAt(i) < 256) {
      hex = '\\x' + cc.charCodeAt().toString(16);

    }
    encoded += hex
  }
  return encoded
}
export {
  encodeForHTMLAttibute,
  encodeForHTML,
  encodeForJavascript
}
