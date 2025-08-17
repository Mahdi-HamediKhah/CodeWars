function queueTime(customers, n) {
  const tills = new Array(n).fill(0);
  for (const customer of customers) {
    let minIndex = tills.indexOf(Math.min(...tills));
    tills[minIndex] += customer;
  }
  return Math.max(...tills);
}


// function queueTime(customers, n) {
//   const tills = Array(n).fill(0);
//   for (const customer of customers) {
//     tills.sort((a, b) => a - b);
//     tills[0] += customer;        
//   }
//   return Math.max(...tills);
// }
