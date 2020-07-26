// import '../CSS/main.css'

function getById(x) {
    return Array.from(document.getElementById(x));
}

function getByClass(x) {
    return Array.from(document.getElementsByClassName(x));
}

// ######################################################################
//                      Features
//  Filtering
//  Sorting +++++++++++++++++++++++++++
//  Paginations ++++++++++++++++++++++
//  Info ++++++++++++++++++++++++++++
//  Page Buttons ++++++++++++++++++++++
//  Ajax Enabled
//  Searching ++++++++++++++++++++++++
//  Column Adjustments
// ######################################################################

let TABLE_CLASS                     = "sw-table";

// Checkboxes Features
let TABLE_CHECKBOXES_ENABLED_CLASS  = "sw-checkboxes";
let TABLE_CHECKBOX_ELEMENT          = '<smart-checkbox id="check-all" checked=false></smart-checkbox>';

// Sorting Features
let TABLE_SORT_CLASS                = "sw-table-sort";
let TABLE_SORT_ICON_UPDOWN          = `<span class="sort-icon">&#8645;</span>`;
let TABLE_SORT_ICON_UP              = `<span class="sort-icon">&#8593;</span>`;
let TABLE_SORT_ICON_DOWN            = `<span class="sort-icon">&#8595;</span>`;

let TABLE_NUMERIC_COL               = "sw-table-numeric";

let TABLE_INFORM_CLASS              = 'sw-table-infom';
let TABLE_ROWER_CLASS               = 'sw-table-rower';
let TABLE_PAGER_CLASS               = 'sw-table-pager';

let TABLE_FILTER_CLASS              = 'sw-table-filter';

let TABLE_SEARCH_CLASS              = 'sw-table-search';

let TABLE_DOTS_CLASS                = 'sw-table-dots';

let TABLE_DOTS_ICON                 = `<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" version="1.1" id="Capa_1" x="0px" y="0px" viewBox="0 0 384 384" style="height:20px;width:20px;cursor:pointer;"><g><g><circle cx="192" cy="42.667" r="42.667"/></g></g><g><g><circle cx="192" cy="192" r="42.667"/></g></g><g><g><circle cx="192" cy="341.333" r="42.667"/></g></g></svg>`;

let TABLE_SEARCH_ICON               = `<svg class="search_icon" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" version="1.1" id="Layer_1" x="0px" y="0px" viewBox="0 0 512 512" style="height:18px; width:20px;padding:2px;cursor: pointer;" xml:space="preserve"><g><g><path d="M508.875,493.792L353.089,338.005c32.358-35.927,52.245-83.296,52.245-135.339C405.333,90.917,314.417,0,202.667,0    S0,90.917,0,202.667s90.917,202.667,202.667,202.667c52.043,0,99.411-19.887,135.339-52.245l155.786,155.786    c2.083,2.083,4.813,3.125,7.542,3.125c2.729,0,5.458-1.042,7.542-3.125C513.042,504.708,513.042,497.958,508.875,493.792z     M202.667,384c-99.979,0-181.333-81.344-181.333-181.333S102.688,21.333,202.667,21.333S384,102.677,384,202.667    S302.646,384,202.667,384z"/></g></g></svg>`;

let TABLE_FILTER_ICON               = `<span class="filter-icon"><svg xmlns="http://www.w3.org/2000/svg" viewBox="-5 0 394 394.00003" style="height:20px;width:20px;" ><path d="m367.820312 0h-351.261718c-6.199219-.0117188-11.878906 3.449219-14.710938 8.960938-2.871094 5.585937-2.367187 12.3125 1.300782 17.414062l128.6875 181.285156c.042968.0625.089843.121094.132812.183594 4.675781 6.3125 7.207031 13.960938 7.21875 21.816406v147.800782c-.027344 4.375 1.691406 8.582031 4.773438 11.6875 3.085937 3.101562 7.28125 4.851562 11.65625 4.851562 2.222656-.003906 4.425781-.445312 6.480468-1.300781l72.3125-27.570313c6.476563-1.980468 10.777344-8.09375 10.777344-15.453125v-120.015625c.011719-7.855468 2.542969-15.503906 7.214844-21.816406.042968-.0625.089844-.121094.132812-.183594l128.691406-181.289062c3.667969-5.097656 4.171876-11.820313 1.300782-17.40625-2.828125-5.515625-8.511719-8.9765628-14.707032-8.964844zm0 0"/></svg></span>`;

let TABLE_NEXT_BTN_ICON             = `<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" version="1.1" viewBox="0 0 477.175 477.175" preserveAspectRatio="none" style="height:1em;width:1.3em; margin:0;padding:0;" xml:space="preserve"><g><path d="M360.731,229.075l-225.1-225.1c-5.3-5.3-13.8-5.3-19.1,0s-5.3,13.8,0,19.1l215.5,215.5l-215.5,215.5   c-5.3,5.3-5.3,13.8,0,19.1c2.6,2.6,6.1,4,9.5,4c3.4,0,6.9-1.3,9.5-4l225.1-225.1C365.931,242.875,365.931,234.275,360.731,229.075z "/></g></svg>`

let TABLE_PREV_BTN_ICON             = `<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" version="1.1" id="Capa_1" x="0px" y="0px" viewBox="0 0 477.175 477.175" preserveAspectRatio="none" style="height:1em;width:1.3em; margin:0;padding:0;" xml:space="preserve"><g><path d="M145.188,238.575l215.5-215.5c5.3-5.3,5.3-13.8,0-19.1s-13.8-5.3-19.1,0l-225.1,225.1c-5.3,5.3-5.3,13.8,0,19.1l225.1,225   c2.6,2.6,6.1,4,9.5,4s6.9-1.3,9.5-4c5.3-5.3,5.3-13.8,0-19.1L145.188,238.575z"/></g></svg>`;

class Table {

    constructor(element) {
        this._element = element;
        this.table_rows = Array.from(element.tBodies[0].rows);
        this.table_cols = Array.from(this._element.tHead.rows[0].cells);
        this.rows_per_page = 5;
        this.current_page = 1;
        this.search_result = false;
        this.footer_span = this.setTableFooter();
        this.total_page = Math.ceil(this.table_rows.length / this.rows_per_page);
        this.featuresEnabled = [];
        this.dir = 'asc';
    }

    DisplayList() {
        Array.from(this.table_rows).forEach(function (elem) {
            elem.style.display = 'none'
        });
        this.current_page--;
        let start = parseInt(this.rows_per_page) * parseInt(this.current_page);
        let end = parseInt(start) + parseInt(this.rows_per_page);
        let paginationItems;
        this.current_page++;
        if (this.search_result) {
            paginationItems = Array.from(this.search_result).slice(start, end);
        } else {
            paginationItems = Array.from(this.table_rows).slice(start, end);
        }
        this._showRows(paginationItems);
    }

    _showRows(selectedRows) {
        for (let i = 0; i < selectedRows.length; i++) {
            selectedRows[i].style.display = 'table-row';
        }
    }

    // TABLE PAGINATION SETUP {TABLE ROWS}, {TABLE INFOM}, {TABLE BUTTONS}
    SetUpPagination() {
        if (this._element.classList.contains(TABLE_INFORM_CLASS)) {
            this.setUpRowsInfo();
            this.featuresEnabled.push('RowsInfo')
        }
        if (this._element.classList.contains(TABLE_ROWER_CLASS)) {
            this.setUpRower();
            this.featuresEnabled.push('Rower')
        }
        if (this._element.classList.contains(TABLE_PAGER_CLASS)) {
            this.setUpPagerInfo();
            this.featuresEnabled.push('PagerInfo')
        }
        this.setUpPrevBtn();
        this.setUpNextBtn();
        this.featuresEnabled.push('PageButtons')

    }

    setUpPagerInfo() {
        let pager_details;
        if (getByClass('pager_details')[0] == undefined) {
            pager_details = document.createElement('span')
            pager_details.classList.add('pager_details')
            this.footer_span.appendChild(pager_details)
        } else {
            pager_details = getByClass('pager_details')[0];
        }
        pager_details.innerText = `${this.current_page} of ${this.total_page} Pages`;
    }

    setUpRowsInfo() {
        let table_rows;
        if (this.search_result) {
            table_rows = this.search_result;
        } else {
            table_rows = this.table_rows;
        }

        let rows_details;

        this.current_page--;

        let start = parseInt(this.rows_per_page) * parseInt(this.current_page);
        let end = parseInt(start) + parseInt(this.rows_per_page);
        let paginationItem = table_rows.slice(start, end);

        this.current_page++;

        if (getByClass('rows_details')[0] == undefined) {
            rows_details = document.createElement('span');
            rows_details.classList.add('rows_details');
            this.footer_span.appendChild(rows_details);
        } else {
            rows_details = getByClass('rows_details')[0];
            this.footer_span.appendChild(rows_details);
        }

        rows_details.innerText = `Showing ${start+1} to ${paginationItem.length + start} of ${table_rows.length} Entries`;

        return paginationItem
    }

    setUpRower() {
        let table_rower;

        if (getByClass('table-rower-wrapper')[0] == undefined) {
            table_rower = document.createElement('span');
            table_rower.classList.add('table-rower-wrapper')
            table_rower.innerHTML = `<small>Show rows</small>
                                    <select class="rower-select" >
                                        <option value="5" >5</option>
                                        <option value="10" >10</option>
                                        <option value="25" >25</option>
                                        <option value="50" >50</option>
                                        <option value="100" >100</option>                                
                                    </select>
                                `;
            this.footer_span.appendChild(table_rower)
            table_rower = getByClass('rower-select')[0];
        } else {
            table_rower = getByClass('rower-select')[0];
        }

        table_rower.onchange = () => {
            this.rows_per_page = getByClass('rower-select')[0].value;
            if (this.search_result) {
                this.total_page = Math.ceil(this.search_result.length / this.rows_per_page);
            } else {
                this.total_page = Math.ceil(this.table_rows.length / this.rows_per_page);
            }
            this.DisplayList();
            this.SetUpPagination();
        }
    }

    setUpNextBtn() {
        let next_btn;

        if (getByClass('next_btn')[0] == undefined) {
            next_btn = document.createElement('button')
            next_btn.classList.add('next_btn');
            next_btn.innerHTML = TABLE_NEXT_BTN_ICON;
            this.footer_span.appendChild(next_btn)
        }

        getByClass('next_btn')[0].onclick = () => {
            if (this.current_page < this.total_page) {
                this.current_page++;
                this.DisplayList();
                this.SetUpPagination();
            }
        }


    }

    setUpPrevBtn() {
        let prev_btn;

        if (getByClass('prev_btn')[0] == undefined) {
            prev_btn = document.createElement('button')
            prev_btn.classList.add('prev_btn');
            prev_btn.innerHTML = TABLE_PREV_BTN_ICON;
            this.footer_span.appendChild(prev_btn);
        }

        getByClass('prev_btn')[0].onclick = () => {
            if (this.current_page > 1) {
                this.current_page--;
                this.DisplayList();
                this.SetUpPagination();
            }
        }

    }

    setTableFooter() {
        let footer, footer_row, footer_span, col;

        if (this._element.tFoot != undefined) {
            footer = this._element.tFoot
            footer_row = footer.children[0]
            footer_span = footer_row.children[0]
        } else {
            footer = this._element.createTFoot();
            footer_row = footer.insertRow(0);
            footer_span = document.createElement('th')
            col = this.table_cols.length
            footer_span.colSpan = col
            footer_row.appendChild(footer_span)
        }
        return footer_span;
    }
    
    // ---------------------------------------------------------------------------------------------
    // Table Sorting 
    EnableTableSorting() {
        Array.from(this.table_cols).forEach((col) => {
            if (col.classList.contains(TABLE_SORT_CLASS)) {
                col.innerHTML += TABLE_SORT_ICON_UPDOWN;                
                col.onclick = () => {
                    this._setTableSorting(this.dir, col.cellIndex);
                    this.DisplayList()
                };
            }
        });
        this.featuresEnabled.push('TableSorting')
    }

    _resetSortIcon() {
        for (let cell of this.table_cols) {
            if (cell.classList.contains(TABLE_SORT_CLASS)) {
                if (cell.children[0]) {                    
                    cell.removeChild(cell.children[0]);
                }
                cell.insertAdjacentHTML('beforeend', TABLE_SORT_ICON_UPDOWN);
            }
        }
    }    

    _setTableSorting(dir, n){
        this._resetSortIcon();
        if(dir == 'asc'){
            if (this.table_cols[n].children[0]) {
                this.table_cols[n].removeChild(this.table_cols[n].children[0]);
            }
            this.table_cols[n].insertAdjacentHTML('beforeend', TABLE_SORT_ICON_UP);

            this._quickSort(this.table_rows, 0, this.table_rows.length - 1, dir, n);
            this.dir = 'dsc';
        }else{
            if (this.table_cols[n].children[0]) {
                this.table_cols[n].removeChild(this.table_cols[n].children[0]);
            }
            this.table_cols[n].insertAdjacentHTML('beforeend', TABLE_SORT_ICON_DOWN);
            
            this._quickSort(this.table_rows, 0, this.table_rows.length - 1, dir, n);
            this.dir = 'asc';
        }
    }

    _swap(items, leftIndex, rightIndex){
        var temp = items[leftIndex];
        items[leftIndex] = items[rightIndex];
        items[rightIndex] = temp;
    }
    
    _partition(items, left, right, dir, n){
        var pivot   = items[Math.floor((right + left) / 2)].children[n].innerText;

        // Dscending Order
        while(left <= right){
            if(dir == 'asc'){
                if(items[left].cells[n].classList.contains(TABLE_NUMERIC_COL)){
                    while (Number(items[left].cells[n].innerText) < Number(pivot)) { left++; }
                    while (Number(items[right].cells[n].innerText) > Number(pivot)) { right--; }
                }else{
                    while (items[left].cells[n].innerText < pivot) { left++; }
                    while (items[right].cells[n].innerText > pivot) { right--; }
                }
            }
            else if (dir == 'dsc'){
                if(items[left].cells[n].classList.contains(TABLE_NUMERIC_COL)){
                    while (Number(items[left].cells[n].innerText) > Number(pivot)) { left++; }
                    while (Number(items[right].cells[n].innerText) < Number(pivot)) { right--; }
                }else{
                    while (items[left].cells[n].innerText > pivot) { left++; }
                    while (items[right].cells[n].innerText < pivot) { right--; }
                }
            }
            if (left <= right) {
                this._swap(items, left, right);
                left++;
                right--;
            }
        }
        return left;
    }

    _quickSort(items, left, right, dir='asc', n){
        var index;

        if (items.length > 1){
            index = this._partition(items, left, right, dir, n);
            if (left < index - 1) {this._quickSort(items, left, index - 1, dir, n);}
            if (index < right) {this._quickSort(items, index, right, dir, n);}
        }

        return items;
    }

    // ---------------------------------------------------------------------------------------------------

    // TABLE FILTER
    setTableFilter() {
        let table_filter = getByClass(TABLE_FILTER_CLASS)[0];

        if (table_filter != undefined) {
            let filter_icon = TABLE_FILTER_ICON

            table_filter.innerHTML = filter_icon;
            table_filter.onclick = (event) => {
                console.log('click');
            }
        }
    }

    // --------------------------------------------------------------------------------------------------
    // TABLE SEARCHBAR
    setTableSearch() {
        let table_search = getByClass(TABLE_SEARCH_CLASS)[0];
        let table_searchbar;

        if (table_search != undefined) {
            let search_icon = TABLE_SEARCH_ICON;
            let search_bar = `<input placeholder="Search.." class="table_searchbar" type="search" />`
            let table_searchbar_wrapper = `<div class="sw-table-searchbar" >${search_icon} ${search_bar}</div>`
            table_search.innerHTML = table_searchbar_wrapper;
            table_searchbar = getByClass('table_searchbar')[0];
        } else {
            table_searchbar = getByClass('table_searchbar')[0];
        }

        table_searchbar.onchange = () => {
            if (table_searchbar.value != "") {
                this.search_result = this._searchInTable(table_searchbar.value);
                this.total_page = Math.ceil(this.search_result.length / this.rows_per_page);
                this.DisplayList();
                this.SetUpPagination();
            } else {
                this.search_result = false;
                this.total_page = Math.ceil(this.table_rows.length / this.rows_per_page);
                this.DisplayList();
                this.SetUpPagination();
            }
        }
        this.featuresEnabled.push('TableSearch');
    }

    _searchInTable(query) {
        let search_result = [];
        for (let i = 0; i < this.table_rows.length; i++) {
            for (let j = 1; j < this.table_rows[i].children.length; j++) {
                if (this.table_rows[i].children[j].innerText.includes(query)) {
                    this.table_rows[i].style.display = 'table-row';
                    search_result.push(this.table_rows[i]);
                } else {
                    this.table_rows[i].style.display = 'none';
                }
            }
        }

        if (search_result.length == 0) {
            let no_search_row = document.createElement('tr')
            let col = this.table_cols.length
            no_search_row.innerHTML = `<td colspan=${col} >No Result Found For ${query} </td>`
            search_result.push(no_search_row)
        }
        return search_result;
    }

    // -------------------------------------------------------------------------------------------------

    setTableDots() {
        let table_dots = getByClass(TABLE_DOTS_CLASS)[0];

        if (table_dots != undefined) {
            let dots_icon = TABLE_DOTS_ICON;
            table_dots.innerHTML = dots_icon;
        }
        this.featuresEnabled.push('TableDots');
    }

    // ------------------------------------------------------------------------------------------------
    // CheckBox Start
    AddCheckboxToTable(){
        // CheckBoxe for Header        
        this._element.tHead.rows[0].insertCell(0);
        this._element.tHead.rows[0].cells[0].innerHTML = TABLE_CHECKBOX_ELEMENT;        
        // CheckBoxes for Body
        for(let i=0; i < this.table_rows.length; i++ ){
                this.table_rows[i].insertCell(0);
                this.table_rows[i].cells[0].innerHTML = `<smart-checkbox id="${'check-'+(i+1)}" checked=false></smart-checkbox>`;
                this.table_rows[i].setAttribute('selected',false);
        }    
        this.footer_span.colSpan = this.table_cols.length + 1
        // CheckBoxes Actions
        let checkboxes = getByClass("checkbox");
        for(let i=0; i < checkboxes.length; i++ ){            
            if(i==0){
                checkboxes[i].onclick = (e) =>{
                    e.preventDefault();
                    this.tick_all(checkboxes, checkboxes[i]);
                    checkboxes[0].parentElement.parentElement.parentElement.bgColor = "#FFF";
                };        
            }else{                
                checkboxes[i].onclick = (e) => {
                    e.preventDefault();                    
                    this.tick_marker(checkboxes[i]);
                    for(let j = 1; j < this.table_rows.length; j++ ){
                        if(checkboxes[j].getAttribute('checked') == 'false'){
                            let real_checkbox = getById(checkboxes[j].htmlFor);
                            checkboxes[j].setAttribute('checked',false)        
                            real_checkbox.checked = false
                            checkboxes[j].children[0].children[0].classList.remove('is-checked')
                            // checkboxes[i].parentElement.parentElement.parentElement.bgColor = "#FFF"
                        }
                    }            
                };
            }
        }
        this.featuresEnabled.push('TableCheckBoxes');
    }
    
    
    tick_all(checkboxes,checkbox){
        if(checkbox.getAttribute('checked') == 'true'){
            for(let i=0; i <checkboxes.length; i++ ){
                this.tick_unchecked(checkboxes[i]);
            }
        }else{
            for(let i=0; i <checkboxes.length; i++ ){
                this.tick_checked(checkboxes[i]);
            }
        }
    }
    
    tick_marker(checkbox){
        if(checkbox.getAttribute('checked') == 'true'){
            this.tick_unchecked(checkbox);
        }else{
            this.tick_checked(checkbox);
        }
    }
    
    tick_checked(checkbox){    
        let real_checkbox = getById(checkbox.htmlFor);    
        checkbox.setAttribute('checked',true)    
        real_checkbox.checked = true;
        checkbox.parentElement.parentElement.parentElement.setAttribute('selected',true)
        checkbox.children[0].children[0].classList.add('is-checked')
        checkbox.parentElement.parentElement.parentElement.bgColor = "#F1F1F1"
    }
    
    tick_unchecked(checkbox){
        let real_checkbox = getById(checkbox.htmlFor);
        checkbox.setAttribute('checked',false)        
        checkbox.parentElement.parentElement.parentElement.setAttribute('selected',false)
        real_checkbox.checked = false
        checkbox.children[0].children[0].classList.remove('is-checked')
        checkbox.parentElement.parentElement.parentElement.bgColor = "#FFF"
    }
    
    getSelectedRows(table_rows){
        let selectedRows = [];
        for(let i=1; i < table_rows.length; i++ ){
            if(table_rows[i].getAttribute('selected') == 'true'){
                selectedRows.push(table_rows[i])
            }
        }
        return selectedRows;            
    }

}

let tables = Array.from(getByClass(TABLE_CLASS));
let f;
tables.forEach( function (table, i) {    
    f = new Table(table);
    // f.AddCheckboxToTable();
    f.EnableTableSorting();
    f.setTableSearch();
    f.setTableDots();
    f.setTableFilter();
    f.DisplayList();
    f.SetUpPagination();
});