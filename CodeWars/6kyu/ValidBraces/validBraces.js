// function validBraces(braces) {
//   let result = braces.split("").reduce((acc, cur) => {
//     cur === "(" ? (acc += 1) : cur === ")" ? (acc -= 1)
//     : cur === "{" ? (acc += 10) : cur === "}" ? (acc -= 10)
//     : cur === "[" ? (acc += 100) : cur === "]" ? (acc -= 100);
//     return acc
//   }, 0);
//
//   return result == 0 ? true : false;
// }

// validBraces("(){}[]");
getSelection