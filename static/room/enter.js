import { callScheduleModal } from "./modals/schedule.js";

let scripts = document.getElementsByTagName('script')
// document.currentScript = document.currentScript || (function () {
//     return scripts[scripts.length - 1];
// })();

const main = [...scripts].filter(sc => sc.src.match(/enter\.js/g)).pop();

const params = main.getAttribute('m');
const decoded = decodeURIComponent(params.replace(/[\+]/g,''));
const jsonData = JSON.parse(decoded);

document.addEventListener('DOMContentLoaded', function () {
    var calendarEl = document.getElementById('calendar');
    var calendar = new FullCalendar.Calendar(calendarEl, {
        initialView: 'dayGridMonth',
        themeSystem: 'bootstrap5',
        headerToolbar: {
            start: 'prevYear,prev,next,nextYear today',
            center: 'title',
            end: 'dayGridMonth,timeGridWeek,timeGridDay'
        },
        navLinks: true,
        weekNumbers: true,
        selectable: true,
        dayHeaders: true,
        locale: navigator.language.split('-').shift(),
        select: function (info) {
            const {startStr:start, endStr:end} = info;
            callScheduleModal(start, end, jsonData[0]);
        }
    });
    calendar.render();
});