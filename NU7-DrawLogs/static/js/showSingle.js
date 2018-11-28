function showSingleBtn() {
    console.log("showSingleBtn is press")
    $("#showAllBox").css('display', 'none')
    $("#showSingleBox").css('display', 'block')
    $.getJSON("./jsonData/data.json", function (data) {
        var myChart = echarts.init(document.getElementById("showSingleBox"));
        myChart.setOption(option = {
            //标题
            title: {
                text: 'Bean.Wei',
                subtext: 'demo test'
            },
            tooltip: {
                trigger: 'axis'
            },
            //图例名
            legend: {
                type:'scroll',
                //show: true,
                orient: 'vertical',//'horizontal', // 'vertical'
                x: 'right',
                y: 'top',
                selectedMode: 'single',
                //selected: selected,
                width: 300,
                align: 'auto',
                borderColor: 'rgba(178,34,34,0.8)',
                borderWidth: 4,
                padding: 10,    // [5, 10, 15, 20]
                marginleft: 10,
                itemGap: 20,
                data: data.map(function (item) {
                    return item.name;
                })
            },
            grid: {
                //top: '10%',
                left: '3%',   //图表距边框的距离
                right: '150',
                bottom: '10%',
                containLabel: true
            },
            //工具框，可以选择
            toolbox: {
                x:'center',
                itemGap: 20,
                feature: {
                    dataZoom: {},
                    dataView: {readOnly: false},
                    restore: {},
                    saveAsImage: {},
                }
            },
            //x轴信息样式
            xAxis: {
                type: 'category',
                boundaryGap: false,
                data: ['12-01','12-02','12-03','12-04','12-05','12-05','12-06','12-07','12-08','12-09','12-10','12-11','12-12','12-13'],
                //坐标轴颜色
                axisLine:{
                    lineStyle:{
                        color:'red'
                    }
                },
                //x轴文字旋转
                axisLabel:{
                    rotate:30,
                    interval:0
                },
            },

            yAxis : [
                {
                    type : 'value',
                    axisLabel : {
                        formatter: '{value} 人'
                    }
                }
            ],
            series: data.map(function(item){
                return {
                    name: item.name,
                    type: item.type,
                    symbol: item.symbol,
                    symbolSize: item.symbolSize,
                    itemStyle: {
                        normal: {
                            color: item.itemStyle.normal.color,
                            borderColor: item.itemStyle.normal.borderColor
                        }
                    },
                    data: item.data.map(function(value) {
                        return value
                    })
                }
            })
        })
    }) 
};