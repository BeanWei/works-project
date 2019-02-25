import { app, remote } from 'electron'
import path from 'path'
import fs from 'fs'

class Store {
    constructor() {
        const dataPath = (app || remote.app).getPath('userData');
        this.path = path.join(dataPath, 'config.json');
        this.config = parseConfig(this.path);
    }

    // 数据测试
    stest() {
        return this.path
    }

    // 获取所有的Projects
    get() {
        return this.config
    }
    // 添加 Projects 数据
    set(cfgObj) {
        /*
        var cfgTmp = {
            "projects": {
                "NU7": {
                    "SPK-THD-UpperLimit" : {
                        "x": [],
                        "y": [],
                        "type": "scatter",
                        "mode": "lines",
                        "name": "SPK-THD-UpperLimit",
                        "line": {
                            "color": "red",
                            "shape": "linear",
                            "width": 1
                        }
                    }
                }
            }
        };
        */
        var projectname = cfgObj.projectname;
        var limitname = cfgObj.limitname;
        if (Object.keys(this.config).length === 0) {
            this.config["projects"] = {};
        }
        this.config["projects"][projectname] = {};
        this.config["projects"][projectname][limitname] = {};
        this.config["projects"][projectname][limitname]["x"] = cfgObj["Xdata"];
        this.config["projects"][projectname][limitname]["y"] = cfgObj["Ydata"];
        this.config["projects"][projectname][limitname]["type"] = "scatter";
        this.config["projects"][projectname][limitname]["mode"] = "lines";
        this.config["projects"][projectname][limitname]["name"] = limitname;
        this.config["projects"][projectname][limitname]["line"] = {};
        this.config["projects"][projectname][limitname]["line"]["color"] = "red";
        this.config["projects"][projectname][limitname]["line"]["shape"] = cfgObj["lineshapetype"];
        this.config["projects"][projectname][limitname]["line"]["width"] = 1;
        clearTimeout(this.saveTimeout);
        this.saveTimeout =setTimeout(() => {
            try {
                fs.writeFileSync(this.path, JSON.stringify(this.config));
            } catch(e) {
                console.error(e);
            }
        }, 2000);
    }
}

function parseConfig(file) {
    if (!fs.existsSync(file)){
        return {};
    }
    try {
        return JSON.parse(fs.readFileSync(file));
    } catch(e) {
        return {};
    }
}

export default new Store();