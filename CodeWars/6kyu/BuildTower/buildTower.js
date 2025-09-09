function towerBuilder(nFloors) {
  let resultTower = Array.from({ length: nFloors }, (_, i) => {
    let spaces = " ".repeat(nFloors -  (i + 1));
    let star = "*".repeat(2 * i + 1);
    return spaces + star + spaces;
  });
  return resultTower;
}

towerBuilder(3);
