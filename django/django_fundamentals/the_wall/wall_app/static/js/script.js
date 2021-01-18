function get_posts() {
    
    $.ajax({url: '/getPost',
        success: function(serverResponse){
            post_list(serverResponse)
          }
      })
       
}

function post_list($array){
    var $html = ''
        for (var i = 0; i < $array.length; i++) {
            var x = $array[i]               
            $html +=   `
                <ul id="${x.id}">
                    <div class="post">
                        <li>
                        <button class="btn btn-danger form-control" onClick="deletePost(${x.id})">DELETE</button> -  ${x.body} <br><br>
                        </li>
                    </div>
                </ul>
                `
        }
    console.log($html)
    document.querySelector("#my_posts").innerHTML = $html;
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

    // $( '.postDelete' ).submit(function(e){
    //     e.preventDefault()
    //     $.ajax({
    //       url: '/deletePost/${x.id}',
    //       method: 'POST',
    //       data: $(this).serialize(),
    //       success: function(serverResponse){
    //           console.log('This is the server response', serverResponse)
    //           get_posts() 
    //           // Replace the html inside a div with the class "posts" with the server response
    //           // $('.post').html(serverResponse)
    //         }
    //     })
    //   })



//     $( '.postDelete/${id}' ).submit(function(e){
//     e.preventDefault()
//     $.ajax({
//       url: '/deletePost/${id}',
//       method: 'POST',
//       data: $(this).serialize(),
//       success: function(serverResponse){
//           console.log('This is deleting a Post')
//           $(el).parents()[1].remove()
//           get_posts() 
//         }
//     })
//   })

function deletePost(id) {
    $.ajax({
      url: `deletePost/${id}`,
      dataType: 'json',
      success: function (data) {
            // $("#" + id).remove(); //type of selectors
            $(`#${id}`).remove(); //type of selectors
    }
  });
}