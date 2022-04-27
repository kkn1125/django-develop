function callScheduleModal(start, end, data) {
    // 초기화
    document.querySelectorAll("#writeModal, [data-bs-target=\"#writeModal\"]").forEach(item=>item.remove());
    // 모달 팝업
    document.querySelector("#app").insertAdjacentHTML("beforeend", `
    <div class="modal fade" id="writeModal" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" aria-labelledby="writeModalLabel" aria-hidden="true">

        <!-- Vertically centered scrollable modal -->
        <div class="modal-dialog modal-dialog-centered modal-dialog-scrollable">
            <div class="modal-content">
                <div class="modal-header">
                    <h5 class="modal-title" id="writeModalLabel">${data.fields.title}</h5>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body">
                    <input type="text" name="title" class="form-control mt-3" placeholder="title">
                    <textarea rows="8" name="desc" class="form-control mt-3" placeholder="description" style="resize: none;"></textarea>
                    <div class="mt-3">
                        <span class="badge text-dark">start</span>
                        <span class="badge text-dark">${start}</span>
                    </div>
                    <div>
                        <span class="badge text-dark">end</span>
                        <span class="badge text-dark">${end}</span>
                    </div>
                </div>
                <div class="modal-footer">
                    <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">닫기</button>
                    <button type="button" class="btn btn-primary">📅 일정 추가</button>
                </div>
            </div>
        </div>
    </div>
    <button hidden type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#writeModal">
    </button>
    `);
    document.querySelector("[data-bs-target=\"#writeModal\"]").click();
}

export {callScheduleModal};