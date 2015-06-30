// 用户数据图
$('.user-charts').highcharts({
    chart: {
        type: 'line'
    },
    title: {
        text: '近期用户数据图'
    },
    xAxis: {
        categories: g.userDates
    },
    yAxis: {
        title: {
            text: '个'
        },
        allowDecimals: false,
        min: 0
    },
    plotOptions: {
        line: {
            dataLabels: {
                enabled: true
            },
            enableMouseTracking: false
        }
    },
    series: [{
        name: '注册用户',
        data: g.userData
    }]
});

// 问题数据图
$('.question-charts').highcharts({
    chart: {
        type: 'line'
    },
    title: {
        text: '近期问题数据图'
    },
    xAxis: {
        categories: g.questionDates
    },
    yAxis: {
        title: {
            text: '个'
        },
        allowDecimals: false,
        min: 0
    },
    plotOptions: {
        line: {
            dataLabels: {
                enabled: true
            },
            enableMouseTracking: false
        }
    },
    series: [{
        name: '提问数',
        data: g.questionData
    }]
});

// 回答数据图
$('.answer-charts').highcharts({
    chart: {
        type: 'line'
    },
    title: {
        text: '近期回答数据图'
    },
    xAxis: {
        categories: g.answerDates,
    },
    yAxis: {
        title: {
            text: '个'
        },
        allowDecimals: false,
        min: 0
    },
    plotOptions: {
        line: {
            dataLabels: {
                enabled: true
            },
            enableMouseTracking: false
        }
    },
    series: [{
        name: '回答数',
        data: g.answerData
    }]
});
