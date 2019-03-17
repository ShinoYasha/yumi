<template>
  <div>
    <div class="UploadCsv">
      <div class="wrapper">
        <div class="title">销售数据</div>
        <div class="desc">
          <strong>导入销售数据</strong>
        </div>
      </div>
      <el-upload
        class="upload-demo"
        action="http://0.0.0.0:5000/upload"
        :on-change="handleChange"
        :on-success="changeList"
        :file-list="fileList3"
        :show-file-list="false"
      >
        <el-button size="small" type="primary">点击上传</el-button>
      </el-upload>
    </div>
    <el-table border :data="tableData" style="width: 100%">
      <el-table-column prop="time" label="起止日期" width="180"></el-table-column>
      <el-table-column prop="source" label="数据来源" width="180"></el-table-column>
      <el-table-column prop="area" label="地区"></el-table-column>
      <el-table-column prop="type" label="数据类型"></el-table-column>
      <el-table-column prop="class" label="玉米种类"></el-table-column>
    </el-table>
  </div>
</template>

<script>
import axios from "axios";
export default {
  data() {
    return {
      fileList3: [],
      tableData: []
    };
  },
  mounted() {
      this.changeList()
  },
  methods: {
    handleChange(file, fileList) {},
    changeList() {
      console.log("123");
      axios.get("http://0.0.0.0:5000/getlist").then(res => {
        console.log(res.data.res);
        this.tableData = res.data.res;
      });
    }
  }
};
</script>

<style <style lang="less" scoped>
.UploadCsv {
  display: flex;
  width: 100%;
  justify-content: space-between;
  margin-top: 100px;
  margin-bottom: 50px;
}
.wrapper {
  margin-left: 10px;
  text-align: left;
}
.desc {
    margin-top: 20px;
}

.upload-demo {
  margin-right: 200px;
}
.title {
  font-size: 40px;
}
.el-upload {
  margin-top: 40px;
}
</style>
