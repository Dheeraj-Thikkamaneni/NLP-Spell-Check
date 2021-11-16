// preparing language file
var aLangKeys=new Array();
aLangKeys['en']=new Array();
aLangKeys['ir']=new Array();

aLangKeys['en']['heading']='SPELL CHECKER';

aLangKeys['en']['sent']='Enter your Sentence';
aLangKeys['en']['sugg']='SUGGESTIONS:';
aLangKeys['en']['res']='Result ';
aLangKeys['en']['reso']='{{result}}';

aLangKeys['ir']['heading']='Seiceálaí Litrithe';

aLangKeys['ir']['sent']='Iontráil d’abairt';
aLangKeys['ir']['sugg']="MOLTAÍ:";
aLangKeys['ir']['res']='Toradh';
aLangKeys['ir']['reso']='{{Toradh}}';


$(document).ready(function() {

    // onclick behavior
    $('.lang').click( function() {
        var lang = $(this).attr('id'); // obtain language id

        // translate all translatable elements
        $('.tr').each(function(i){
          $(this).text(aLangKeys[lang][ $(this).attr('key') ]);
        });

    } );

});