class SmartCheckBox extends HTMLElement{    
    constructor(){
        super();
        this.innerHTML = `
                            <label for="${this.getAttribute('id')}" class="checkbox" checked=${this.getAttribute('checked')}>
                                <span class="checkbox_box-outline">
                                    <span class="checkbox_tick-outline"></span>
                                </span>
                                <input type="checkbox" class="checkbox-input" id="${this.getAttribute('id')}">
                            </label>
                        `;
    }

}

window.customElements.define('smart-checkbox',SmartCheckBox);

