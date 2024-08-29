function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
  }
  function cancel(i)
  {
    var rows=$('#proj-table tbody tr').eq(i);
            const cells = rows.children('td');
                  // Loop through cells and log their contents
                  cells.each(function(index) {
                      var input=$(this).children('input')
                      console.log(`cancel ${index}: ${input.val()}`);
                      var valu=input.val();
                      $(this).empty()
                      $(this).text(valu)
                      if( index == 7)
                      $(this).html('<button class="edi button-34" onclick="permission()" ><i class="fas fa-edit"></button></i>')
                      $('#act-btn').empty()
                    })
  
  }
  function cancelOP(i)
  {
    var rows=$('#opr-table tbody tr').eq(i);
            const cells = rows.children('td');
                  // Loop through cells and log their contents
                  cells.each(function(index) {
                      var input=$(this).children('input')
                      console.log(`cancel ${index}: ${input.val()}`);
                      var valu=input.val();
                      $(this).empty()
                      $(this).text(valu)
                      if( index == 12)
                      $(this).html('<button class="edi button-34" onclick="permissionOP()" ><i class="fas fa-edit"></button></i>')
                      $('#act-btn').empty()
                    })
  
  }
  function permission(){
    $(document).ready(function(){
        urls='/projet/update/'
      $('.edi').on('click',function()
    {
      var list=new Array()
      var row=$(this).closest('tr')
      row.find("td").not(":last").each(function(index) {  
                // Get the current text of the cell
                var cellText = $(this).text();
    
                // Replace the cell content with an input field containing the current text
                switch (true) {
                          case index == 0:
                          $(this).html('<input type="text" value="'+cellText+'" id="editcell'+index+'" disabled />')
                            break;
                          case index == 3 || index == 4 || index == 5:
                            var nowhite=cellText.replace(/\s+/g, '');
                            var inte=parseInt(nowhite);
                          $(this).html('<input class="td-edit"  type="number" step="0.01" name="PEC" value="'+inte+'" id="editcell'+index+'" />')
                            break;
                            case index == 6 :
                            $(this).html('<input class="td-edit" type="text" value="'+cellText+'" id="editcell'+index+'" />')
                              break;
                              default:
                          $(this).html('<input class="td-edit" type="text" value="'+cellText+'" id="editcell'+index+'"  />')
                            break;
                }
            });
            var indexss=row.index()
            var parent=$(this).parent()
            $(this).parent().empty();
            parent.html('<button class="button-34" id="cnl-btn" onclick=cancel('+indexss+')><i class="fas fa-sign-out-alt"></i></button>')
            $('#act-btn').html('<button class="button-34" id="sv-btn")><i class="far fa-check-circle"></i></button>')
            $(document).on('click','#sv-btn',function()
            {
              row.find("td").not(":last").each(function(index) {  
                // Get the current text of the cell
                var cellText = $(this).text();
                  console.log(' cell '+index+' value '+$(this).find('input').val())
                  list.push($(this).find('input').val())
                // Replace the cell content with an input field containing the current text
            });
            var formData = new FormData();
    
            console.log(' form data lengh '+list.length+' value '+JSON.stringify(list))
           
             ;
             
              formData.append('id_projet',list[0])
              formData.append('Libelle',list[1])
              formData.append('num_indiv',list[2])
              formData.append('AP_Act',list[3])
              formData.append('dp_cum',list[4])
              formData.append('PEC',list[5])
              formData.append('dp_prev',list[6])
              $.ajax({
                url: urls,  // Replace with your Django view URL
                type: 'POST',
                data: formData,
                processData: false,  // Prevent jQuery from automatically transforming the data into a query string
                contentType: false,  // Prevent jQuery from overriding the Content-Type header
                headers: {
                    'X-CSRFToken': getCookie('csrftoken') // Include CSRF token for security
                },
                success: function(response) {
                    console.log('Success:', response.message);
                    cancel(indexss)
                },
                error: function(xhr, status, error) {
                    console.log('Error:', error);
                }
            });
              })
            })
    })
    }

    function permissionOP(){
        urls='/operation/update/'
        $(document).ready(function(){
          $('.edi').on('click',function()
        {
          var list=new Array()
          var row=$(this).closest('tr')
          row.find("td").not(":last").each(function(index) {  
                    // Get the current text of the cell
                    var cellText = $(this).text();
        
                    // Replace the cell content with an input field containing the current text
                    switch (true) {
                              case index == 0:
                              $(this).html('<input type="text" value="'+cellText+'" id="editcell'+index+'" disabled />')
                                break;
                              case index == 3 || index == 4 || index == 5:
                                var nowhite=cellText.replace(/\s+/g, '');
                                var inte=parseInt(nowhite);
                              $(this).html('<input class="td-edit"  type="text" name="PEC" value="'+inte+'" id="editcell'+index+'" />')
                                break;
                                case index == 6 :
                                $(this).html('<input class="td-edit" type="text" value="'+cellText+'" id="editcell'+index+'" />')
                                  break;
                                  default:
                              $(this).html('<input class="td-edit" type="text" value="'+cellText+'" id="editcell'+index+'"  />')
                                break;
                    }
                });
                var indexss=row.index()
                var parent=$(this).parent()
                $(this).parent().empty();
                parent.html('<button class="button-34" id="cnl-btn" onclick=cancelOP('+indexss+')><i class="fas fa-sign-out-alt"></i></button>')
                $('#act-btn').html('<button class="button-34" id="sv-btn")><i class="far fa-check-circle"></i></button>')
                $(document).on('click','#sv-btn',function()
                {
                  row.find("td").not(":last").each(function(index) {  
                    // Get the current text of the cell
                    var cellText = $(this).text();
                      console.log(' cell '+index+' value '+$(this).find('input').val())
                      list.push($(this).find('input').val())
                    // Replace the cell content with an input field containing the current text
                });
                var formData = new FormData();
        
                console.log(' form data lengh '+list.length+' value '+JSON.stringify(list))
               
                 ;
                 
                  formData.append('id_libelle_op',list[0])
                  formData.append('num_op',list[1])
                  formData.append('object_vise_po',list[2])
                  formData.append('notifcation_an_MF_op',list[3])
                  formData.append('indiv_an_op',list[4])
                  formData.append('AP_init_op',list[5])
                  formData.append('AP_real_op',list[6])
                  formData.append('cum_AP_eng_an_op',list[7])
                  formData.append('cum_AP_pai_an_op',list[8])
                  formData.append('taux_real_ph_an_op',list[9])
                  formData.append('date_cre_op',list[10])
                  $.ajax({
                    url: urls,  // Replace with your Django view URL
                    type: 'POST',
                    data: formData,
                    processData: false,  // Prevent jQuery from automatically transforming the data into a query string
                    contentType: false,  // Prevent jQuery from overriding the Content-Type header
                    headers: {
                        'X-CSRFToken': getCookie('csrftoken') // Include CSRF token for security
                    },
                    success: function(response) {
                        console.log('Success:', response.message);
                        cancelOP(indexss)
                    },
                    error: function(xhr, status, error) {
                        console.log('Error:', error);
                    }
                });
                  })
                })
        })
        }