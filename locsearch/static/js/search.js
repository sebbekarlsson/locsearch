document.addEventListener('DOMContentLoaded', function(e){
    var app = new Vue({
        el: '#app',
        data: {
            message: '',
            results: []
        },
        methods: {
            onSearch: function(e) {
                var _this = this;

                if (e.target.value.length >= 3)
                request('/api/search/SE/' + e.target.value, 'GET', {}, function(data){
                   _this.results = JSON.parse(data);
                });
            }
        }
    })
});
