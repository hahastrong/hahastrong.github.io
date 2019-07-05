//资金流
                            var _dh = dataArr[0].split(',');
                            var _ds = dataArr[1].split(',');
                            //算和值
                            var data = [];

                            var total = (parseFloat(_dh[7]) + parseFloat(_dh[11]) + parseFloat(_dh[15]) + parseFloat(_dh[19]) +
                                parseFloat(_ds[7]) + parseFloat(_ds[11]) + parseFloat(_ds[15]) + parseFloat(_ds[19])) / 100000000;

                            data[0] = (_dh[5] == "" || _ds[5] == "") ? "" : ((parseFloat(_dh[5]) + parseFloat(_ds[5])) / 10000).toFixed(4);//今日主力净流入
                            data[1] = (data[0] * 100 / total).toFixed(2);//主力净比


                            data[2] = (_dh[9] == "" || _ds[9] == "") ? "" : ((parseFloat(_dh[9]) + parseFloat(_ds[9])) / 10000).toFixed(4);//今日超大单净流入
                            data[3] = (data[2] * 100 / total).toFixed(2);//主力净比


                            data[4] = (_dh[13] == "" || _ds[13] == "") ? "" : ((parseFloat(_dh[13]) + parseFloat(_ds[13])) / 10000).toFixed(4);//今日大单净流入
                            data[5] = (data[4] * 100 / total).toFixed(2);//主力净比

                            data[6] = (_dh[17] == "" || _ds[17] == "") ? "" : ((parseFloat(_dh[17]) + parseFloat(_ds[17])) / 10000).toFixed(4);//今日中单净流入
                            data[7] = (data[6] * 100 / total).toFixed(2);//主力净比

                            data[8] = (_dh[21] == "" || _ds[21] == "") ? "" : ((parseFloat(_dh[21]) + parseFloat(_ds[21])) / 10000).toFixed(4);//今日小单净流入
                            data[9] = (data[8] * 100 / total).toFixed(2);//主力净比

                            data[10] = '';//
                            data[11] = '';//
                            data[12] = (_dh[7] == "" || _ds[7] == "") ? "" : ((parseFloat(_dh[7]) + parseFloat(_ds[7])) / 100000000).toFixed(4);//超大单流入
                            data[13] = (_dh[8] == "" || _ds[8] == "") ? "" : ((parseFloat(_dh[8]) + parseFloat(_ds[8])) / 100000000).toFixed(4);//超大单流处
                            data[14] = (_dh[11] == "" || _ds[11] == "") ? "" : ((parseFloat(_dh[11]) + parseFloat(_ds[11])) / 100000000).toFixed(4);//大单流入
                            data[15] = (_dh[12] == "" || _ds[12] == "") ? "" : ((parseFloat(_dh[12]) + parseFloat(_ds[12])) / 100000000).toFixed(4);//大单流出
                            data[16] = (_dh[15] == "" || _ds[15] == "") ? "" : ((parseFloat(_dh[15]) + parseFloat(_ds[15])) / 100000000).toFixed(4);//中单流入
                            data[17] = (_dh[16] == "" || _ds[16] == "") ? "" : ((parseFloat(_dh[16]) + parseFloat(_ds[16])) / 100000000).toFixed(4);//中单流出
                            data[18] = (_dh[19] == "" || _ds[19] == "") ? "" : ((parseFloat(_dh[19]) + parseFloat(_ds[19])) / 100000000).toFixed(4);//小单流入
                            data[19] = (_dh[20] == "" || _ds[20] == "") ? "" : ((parseFloat(_dh[20]) + parseFloat(_ds[20])) / 100000000).toFixed(4);//小单流出
