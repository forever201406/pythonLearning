$('.uk-modal').on({

    'show.uk.modal': function(){
        //得到要请求的文件的url
        var url = window.location.protocol + "//" + window.location.host + "/search.xml";

        $.ajax({
            url: url,
            dataType: "xml",
            success: function( xmlResponse ) {
                //获取xml文件中的数据
                var datas = $( "entry", xmlResponse ).map(function() {
                    return {
                        title: $( "title", this ).text(),
                        content: $("content",this).text(),
                        url: $( "url" , this).text()
                    };
                }).get();

                var $input = document.getElementById('my-search-input');
                var $searchContent = document.getElementById('search-content');

                $input.addEventListener('input', function(){
                    var str='';
                    var flags = [];                    //用来标记那几篇文章里包含搜索的关键字
                    var content_index = [];
                    var keywords = this.value.trim().split(/[\s\-]+/);

                    $searchContent.innerHTML = "";

                    //在文章的标题和内容里对关键字进行搜索
                    keywords.forEach(function(keyword){
                        if(keyword != ''){
                            var keyword_len = keyword.length;
                            datas.forEach(function(data , i){
                                var data_title = data.title.trim();
                                var data_content = data.content.trim().replace(/<[^>]+>/g,"");
                                var index_title = -1;
                                var index_content = -1;

                                //只有当文章的标题和内容都不为空的时候才对文章进行匹配
                                if(data_title != '' && data_content != ''){
                                    index_title = data_title.indexOf(keyword);
                                    index_content = data_content.indexOf(keyword);
                                }

                                if( index_title >= 0 || index_content >= 0 ){
                                    if(flags.indexOf(i) == -1) {
                                        flags.push(i);
                                        content_index.push({index_content:index_content, keyword_len:keyword_len});
                                    }
                                }
                            });
                        }
                    });

                    //展示搜索到的结果
                    if(flags != []){
                        flags.forEach(function(flag , i){
                            var post_url = datas[flag].url;
                            var post_title = datas[flag].title;

                            str += "<li><a href='"+ post_url +"' class='list-title'>"+ post_title +"</a>";

                            var content = datas[flag].content.trim().replace(/<[^>]+>/g,"");
                            var ind = content_index[i].index_content;
                            var keyword_len = content_index[i].keyword_len;

                            if(ind >= 0){
                                //截取100个字符,确定截取的起始位置
                                var start = ind - 20;
                                var end = ind + 80;

                                if(start < 0){
                                    start = 0;
                                }

                                if(start == 0){
                                    end = 100;
                                }

                                if(end > content.length){
                                    end = content.length;
                                }

                                var before_content = content.substr(start, ind - start);
                                var key_content = content.substr(ind, keyword_len);
                                var after_content = content.substr(ind + keyword_len, end - ind - keyword_len);

                                str += "<p" +" class='list-content'>" + before_content;
                                str += "<span" + " class='span-content'" + ">" + key_content +"</span>";
                                str += after_content +"...</p>"
                            }

                            str += "</li>";
                        });
                    }

                    $searchContent.innerHTML = str;
                });
            }
        });
    },

    'hide.uk.modal': function(){
        var $input = document.getElementById('my-search-input');
        var $searchContent = document.getElementById('search-content');

        $input.value = '';
        $searchContent.innerHTML = '';
    }
});
