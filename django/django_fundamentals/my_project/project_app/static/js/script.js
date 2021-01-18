    function get_posts() {
    
        $.ajax({url: '/seeTheCrowdJson',
            success: function(serverResponse){
                post_list(serverResponse)
              }
          })
           
    }
    
    function post_list($array){
        var $html = ''
        var users = $array.users
        var logIn = $array.loggedIn[0]
        function filter_user(id){
            var usersobj = {}
            for (let i = 0; i < users.length; i++) {
                if (users[i].id == id){
                    usersobj = users [i]
                } 
            }
            return usersobj
        }
            for (var i = 0; i < $array.posts.length; i++) {
                var wallPost = $array.posts[i]
                $html +=   `
                <div class="flex-fill blogPost" cstyle="border-style: solid;border-color: var(--danger);padding: 20px;">
                <p> <a href="profile/${wallPost.usersPost_id}">${filter_user(wallPost.usersPost_id).first} ${filter_user(wallPost.usersPost_id).last}</a></p>
                <p class="blogBody" style="border-style: solid;border-color: var(--dark);">${wallPost.body} </p>
                <p class="postTime">${moment(wallPost.updated_at).format('LLLL')} </p>
                <form action="newReply" method="post">
                                        {%csrf_token%}
                                        <input type="text" name="reply">
                                        <input type="hidden" name="postId" value='{{wallPost.id}}'>
                                        <input type="submit" value="reply">
                                    </form>
                <div class="btn-group"><button class="btn btn-primary" type="submit">Reply </button>
                `             
                if (logIn.id ==  wallPost.usersPost_id){                   
                $html +=    `<button class="btn btn-primary dropdown-toggle dropdown-toggle-split" data-toggle="dropdown" aria-expanded="false" type="button"></button>
                    <div class="dropdown-menu">
                        <a class="dropdown-item" href="/deleteCrowdPost/${wallPost.id}">Delete</a>
                        <a class="dropdown-item" href="#">Edit</a>
                        <a class="dropdown-item" href="#"></a>
                    </div>`
            }
                $html +=   `</div>
        </div>`
            }
        document.querySelector("#wall_post").innerHTML = $html;
    }
    
    
    get_posts()  
    
    $( '#postForm' ).submit(function(e){
      e.preventDefault()
      $.ajax({
        url: '/newPost',
        method: 'POST',
        data: $(this).serialize(),
        success: function(serverResponse){
            console.log('This is the server response', serverResponse)
            get_posts() 
            // Replace the html inside a div with the class "posts" with the server response
            // $('.post').html(serverResponse)
          }
      })
    })