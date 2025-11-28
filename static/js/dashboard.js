// Extract data
let departments = dataFromDB.map(row => row.department);
let ratings = dataFromDB.map(row => row.rating);

// Department count
let deptCounts = {};
departments.forEach(d => deptCounts[d] = (deptCounts[d] || 0) + 1);

Plotly.newPlot('chart-dept', [{
    x: Object.keys(deptCounts),
    y: Object.values(deptCounts),
    type: 'bar'
}], { title: "Responses by Department" });


// Ratings histogram
Plotly.newPlot('chart-rating', [{
    x: ratings,
    type: 'histogram'
}], { title: "Rating Distribution" });


