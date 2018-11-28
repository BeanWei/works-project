function showSingleBtn() {
    console.log("showSingleBtn is press")
    $("#showAllBox").css('display', 'none')
    $("#showSingleBox").css('display', 'block')
    $.getJSON("./jsonData/data.json", function (data) {
        var myChart = echarts.init(document.getElementById("showSingleBox"));
        myChart.setOption(option = {
            //标题
            title: {
                text: 'NU7-Audio',
                subtext: 'QCMC·AudioTeam'
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
                //width: 50,
                //align: 'auto',
                align: 'left',
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
                top: '10%',
                left: '1%',   //图表距边框的距离
                right: '26%',
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
                data: [100.00,106.00,112.00,118.00,125.00,132.00,140.00,150.00,160.00,170.00,180.00,190.00,200.00,212.00,224.00,236.00,250.00,265.00,280.00,300.00,315.00,335.00,355.00,375.00,400.00,425.00,450.00,475.00,500.00,530.00,560.00,600.00,630.00,670.00,710.00,750.00,800.00,850.00,900.00,950.00,1000.00,1060.00,1120.00,1180.00,1250.00,1320.00,1400.00,1500.00,1600.00,1700.00,1800.00,1900.00,2000.00,2120.00,2240.00,2360.00,2500.00,2650.00,2800.00,3000.00,3150.00,3350.00,3550.00,3750.00,4000.00,4250.00,4500.00],
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
                        formatter: '{value} db'
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