/**~！！=> 这里固定了提交Btn的ID.
 * 筛选数据的公共方法
 * selectType: 选择处理数据的方式，筛除 or 选择
 * 返回筛选后的数据
 */
function filterData(data, selectType) {
    var rule1 = $('#softReg').val();
    var rule2 = $('#exactReg').val();
    var rule30 = $('#minY').val();
    var rule31 = $('#maxY').val();
    var rule = "";
    var ruleType = -1;
    if (rule1 == "") {
        if (rule2 == "") {
            if (rule30 == "" && rule31 == "") {
                alert("请输入筛选规则")
            } else if (rule30 == "" || rule31 == "") {
                alert("请输入最小值或最大值")
            } else {
                var rule30int = parseFloat(rule30);
                var rule31int = parseFloat(rule31);
                if (isNaN(rule30int) || isNaN(rule31int)) {
                    alert("范围只能填入数字")
                } else{
                    if (rule30int < rule31int) {
                        rule = rule30 + "," + rule31;
                        ruleType = 3;
                    } else if (rule30int > rule31int) {
                        rule = rule31 + "," + rule30;
                        ruleType = 3;
                    } else {
                        alert("最小值和最大值不能相等")
                    }
                }
                    
            }
        } else {
            rule = rule2;
            ruleType = 2;
        }
    } else {
        rule = rule1;
        ruleType = 1;
    };
    var result = new Array();
    for (var i in data) {
        //保留limit, 不做任何判断。
        if (data[i].name.indexOf("Limit") != -1) {
            result.push(data[i])
        } else {
            if (ruleType == 1) {
                //这里模糊匹配暂用最简单的方法：判断曲线的名称字符内是否包含输入的字符
                if (data[i].name.indexOf(rule) != -1) {
                    result.push(data[i])
                }
            } else if (ruleType == 2) {
                lineNameList = rule.split("\n")
                if (selectType == "select") {
                    if (lineNameList.indexOf(data[i].name) != -1) {
                        result.push(data[i])
                    }
                } else if (selectType == "ignore") {
                    if (lineNameList.indexOf(data[i].name) == -1) {
                        result.push(data[i])
                    }
                }
                
            } else if (ruleType == 3) {
                range = rule.split(",")
                minY = range[0]
                maxY = range[1]
                if (Math.min.apply(null, data[i].data) > minY && Math.max.apply(null, data[i].data) < maxY) {
                    result.push(data[i])
                }   
            }
        }     
    };
    return result
};
