function showSingleBtn() {
    console.log("showSingleBtn is press")
    $("#showAllBox").css('display', 'none')
    $("#showSingleBox").css('display', 'block')
    $.getJSON("../jsonData/Spk_THD.json", function (data) {
        var myChart = echarts.init(document.getElementById("showSingleBox"));
        myChart.setOption(option = {
            //标题
            title: {
                text: 'Spk_THD',
                subtext: 'NU7'
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
                left: '0%',   //图表距边框的距离
                right: '30%',
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
                data: [100,106,112,118,125,132,140,150,160,170,180,190,200,212,224,236,250,265,280,300,315,335,355,375,400,425,450,475,500,530,560,600,630,670,710,750,800,850,900,950,1000,1060,1120,1180,1250,1320,1400,1500,1600,1700,1800,1900,2000,2120,2240,2360,2500,2650,2800,3000,3150,3350,3550,3750,4000,4250,4500,4750,5000,5300,5600,6000,6300,6700,7100,7500,8000,8500,9000,9500,10000,10600,11200,11800,12500,13200,14000,15000,16000,17000,18000,19000,20000,21200,22400],
                //坐标轴颜色
                // axisLine:{
                //     lineStyle:{
                //         color:'red'
                //     }
                // },
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
                        formatter: '{value}'
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