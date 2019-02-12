var socket = io.connect("http://" + document.domain + ":" + location.port);

socket.on("connect", function () {
	socket.emit("fetch new message")
	var form = $("form").on("submit", function (e) {
		e.preventDefault()
		let user_input = $("input.message").val()
		socket.emit("send message", {
			message: user_input
		})
		$("input.message").val("").focus()
	})

	var getNewMessage = $("#getNewMessage").on("click", function () {
		socket.emit("fetch new message")
	})

	var addLike = $("#addLike").on("click", function () {
		socket.emit("add like", {
			id: 1
		})
	})
})

socket.on("send new message to client", function (msg) {
	console.log(msg)
	$("div.message_holder").append($("<div>" +
		msg.message + "</div>"))
})