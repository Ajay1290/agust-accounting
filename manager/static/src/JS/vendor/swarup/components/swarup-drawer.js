const drawers = Array.from(document.querySelectorAll('.drawer'));
const drawer_buttons = Array.from(document.querySelectorAll('.drawer-button'));

const drawer_c_buttons = Array.from(document.querySelectorAll('.drawer-cancle-button'));

drawers.forEach(function(drawer, index){    
    drawer_c_buttons.forEach(function(btn, index){        
        let open_Drawers = [];
        open_Drawers.push(drawer);
        btn.addEventListener('click', function(e){
            e.stopImmediatePropagation()
            if(document.querySelector('.backdrop')){
                removeBackdropElement(open_Drawers);
            }
        })
    })
    drawer_buttons.forEach(function(btn, index){
        let target_modal = btn.getAttribute('drawer-target');
        let modal_list = Array.from(document.querySelectorAll(target_modal));        
        btn.addEventListener('click', function(e){            
            e.stopImmediatePropagation()
            if(document.querySelector('.backdrop')){                                
                removeBackdropElement(modal_list);
            }else{                                
                addBackdropElement(modal_list);
            }
        })
    })    
})

function addBackdropElement(lis){
    try {
        lis[0].classList.add('is__opening');   
        setTimeout(function(){        
            let backdrop = document.createElement('div');
            backdrop.classList.add('backdrop');    
            document.body.appendChild(backdrop);
            backdrop.classList.add('active');
            lis[0].classList.remove('is__opening')
            lis[0].classList.add('active')        
            backdrop.addEventListener('click', () =>{
                removeBackdropElement(lis)        
            })
            document.body.style.overflow = "hidden";
        },300)   
    } catch (error) {
        console.log('Do you forget to asign modal-target attribute to button');
    }    
}

function removeBackdropElement(lis){    
    try {
        let backdrop = document.querySelector('.backdrop');    
        backdrop.classList.remove('active');
        backdrop.classList.add('is__closeing');        
        lis[0].classList.add('is__closeing')
        setTimeout(function(){
            lis[0].classList.remove('is__closeing')
            lis[0].classList.remove('active')                
            document.body.removeChild(backdrop);
            document.body.style.overflow = "auto";
        },300)   
    } catch (error) {
        console.log(error);
    }
}