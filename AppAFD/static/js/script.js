$('input[type=file]').change(function(){
    if($('input[type=file]').val()==''){
        $('#btnImport').attr('disabled',true)
    }
    else{
        $('#btnImport').attr('disabled',false);
    }
})

$('input[type=cbEmployees]').change(function(){
    if($('input[type=file]').val()=='FUNCIONÁRIO'){
        $('#btnPrint').attr('disabled',true)
    }
    else{

    }
})