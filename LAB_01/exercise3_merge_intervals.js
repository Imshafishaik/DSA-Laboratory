function mergeIntervals(intvals) {
    if (intvals.length <= 1) return intvals;

    intvals.sort((a, b) => a[0] - b[0]);

    const merged = [];
    let current = intvals[0];

    for (let i = 1; i < intvals.length; i++) {
        const next = intvals[i];

        if (next[0] <= current[1]) {
            current[1] = Math.max(current[1], next[1]);
        } else {
            merged.push(current);
            current = next;
        }
    }

    merged.push(current);
    return merged;
}

console.log(mergeIntervals([[1,3],[2,6],[8,10],[15,18]]));