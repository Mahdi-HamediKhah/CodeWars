function checkout(time) {
  return new Promise((resolve) => {
    setTimeout(() => {
      resolve(time);
    }, time);
  });
}

async function queueTime(customers, n) {
  let queue = [];
  for (const customer of customers) {
    const promise = checkout(customer);
    queue.push(promise);

    if (queue.length >= n) {
      const finished = await Promise.race(queue);
      queue = queue.filter(promise => promise !== finished);
    }
  }
}

queueTime([2, 2, 3, 3, 4, 4], 2);
