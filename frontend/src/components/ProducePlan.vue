<template>
    <div>
        <div class="wrapper">
            <div class="title">销售数据</div>
            <div class="desc">
                <strong>数据管理</strong>
            </div>
        </div>
        <div class="title1">制定计划</div>
        <div class="row">
            <div class="row">计划名称
                <el-input v-model="name" size="small" placeholder="请输入内容"></el-input>
            </div>
            <div class="row">
                计划量A
                <el-input v-model="heiyumi" size="small" placeholder="请输入内容"></el-input> 
                品类：黑玉米
            </div>
            <div class="row">
                计划量B
                <el-input v-model="huayumi" size="small" placeholder="请输入内容"></el-input> 
                品类：花玉米
            </div>
            <div class="row">
                计划量C
                <el-input v-model="tianyumi" size="small" placeholder="请输入内容"></el-input> 
                品类：甜玉米
            </div>
            <div class="row">
                <el-input
                    type="textarea"
                    :rows="2"
                    placeholder="备注"
                    v-model="textarea">
                </el-input>

            </div>
        </div>
        <el-button type="primary" @click="submitPlan">确定</el-button>
    </div>
</template>
<script>
import axios from 'axios'
export default {
    data() {
        return {
            name: '',
            value: '',
            value1: '',
            heiyumi: '',
            huayumi: '',
            tianyumi: '',
            options: [],
            tableData: [],
            textarea: ''
        }
    },
    methods: {
        getList() {
            axios.get("http://0.0.0.0:5000/getlist").then(res => {
                this.tableData = res.data.res
                for(let i in this.tableData) {
                    console.log(i)
                    let o = {
                        value: i,
                        label: this.tableData[i].class
                    }
                    console.log(o)
                    this.options.push(o)
                }
            })
        },
        submitPlan() {
            axios.get('http://0.0.0.0:5000/submitplan', {
                params: {
                    name: this.name,
                    heiyumi: this.heiyumi,
                    huayumi: this.huayumi,
                    tianyumi: this.tianyumi,
                    textarea: this.textarea,
                    key: new Date().getTime()
                }
            }).then(res => {
                
            })
        }
    }
}
</script>

<style lang="less" scoped>
.el-input {
    width: 20%;
}
.el-textarea {
    width: 70%;
}
.wrapper {
    margin-top: 100px;
    margin-left: 10px;
    text-align: left;
    .title {
        font-size: 40px;
    }
    .desc {
        margin-top: 20px;
    }
}
    .title1 {
        text-align: left;
        padding: 10px;
        background: #eeeeee;
    }
.row {
    margin: 30px;
    text-align: left;

    .row {
        // display: flex;
    }
}
</style>
