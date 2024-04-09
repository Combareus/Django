
function addday(){

    var list = document.getElementById("days");
    list.innerHTML += `<li class="cd-schedule__group"><div class="cd-schedule__top-info"><span>day${(list.children.length + 1)%7}</span></div></li>`;
}
function test(timestart, timeend, eventsample, dataevent){
    var list = document.getElementById("MMDDYYYY");
    list.write() +=
    `<li class="cd-schedule__event">
        <a data-start=${timestart} data-end=${timeend}  data-content=${eventsample} data-event=${dataevent} href="#0">
        <em class="cd-schedule__name">Smple</em>
        </a>
    </li>`;
    console.log("checkpoints");
}