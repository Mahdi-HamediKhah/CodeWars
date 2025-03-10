function findShort(s) {
  const words = s.split(" ");
  let wordsLength = words[0].length;
  for (const word of words) {
    if (word.length < wordsLength) {
      wordsLength = word.length;
    }
  }
  return wordsLength;
}