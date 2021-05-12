const chekBoxML = document.querySelector('#aaa1')
const buttonResult = document.querySelector('#result')

console.log(buttonResult)

buttonResult.addEventListener('click', function(){
    
    if (chekBoxML.checked){
        console.log ("Все работет")
        return 1
    }else{
        console.log("НЕ сработало")
    }
    
})
