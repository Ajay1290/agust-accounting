var PANEL_CLASS = 'sw-panel';
var PANEL_WING_CLASS = 'sw-wing';
var WING_BTN_CLASS = 'wing-btn';
var DATA_WING_ATTRIBUTE = 'data-wing';
var DATA_TARGET_ATTRIBUTE = 'data-target';        
var SHOW_CLASS = 'show';
var panels;
panels = Array.from(document.getElementsByClassName(PANEL_CLASS));
panels.forEach(panel => {
    var wings = {};
    var btns = [];
    var active_wing;
    
    Array.from(panel.children).forEach(wing => {
        
        if (wing.classList.contains(SHOW_CLASS)){
            active_wing = wing;
        }

        if(wing.classList.contains(PANEL_WING_CLASS)){                    
            wings[wing.getAttribute(DATA_WING_ATTRIBUTE)] = wing;                    
        }

        Array.from(wing.children).forEach(btn => {               
            if(btn.classList.contains(WING_BTN_CLASS)){
                var target_dict = [];
                target_dict[0] = btn.getAttribute(DATA_TARGET_ATTRIBUTE)
                target_dict[1] = btn;
                btns.push(target_dict);
            }
        });                

    });

    btns.forEach(btnlist => {
        var target = btnlist[0];
        var btn = btnlist[1];                
        btn.addEventListener('click', function(evet){                    
            active_wing.classList.remove(SHOW_CLASS);
            wings[target].classList.add(SHOW_CLASS);
            active_wing = wings[target];
        });                
    });


});