let mysketch = (p) => {

	let cwidth = 500
    let cheight = 500
    let defaultBrushWeight = cwidth / 300
    let eraserWeight = defaultBrushWeight * 10
    let currentWeight = defaultBrushWeight

    let smallgfx;
    let gfx;

	let isErasing;

    p.setup = () => {

        cnv = p.createCanvas(cwidth, cheight)
        cnv.parent('canvasContainer')
        gfx = p.createGraphics(cwidth, cheight)

		smallgfx = p.createGraphics(128,128)
		let resultImg = document.getElementById("resultImg")
        let eraserToggle = document.getElementById("eraserToggle")
        let btn = document.getElementById("convertButton")
        let eraserSlider = document.getElementById("eraserSizeSlider")
		let extraImagesDiv = document.getElementById("extraImages")
		let clearButton = document.getElementById("clear")

		cnv.dragOver(highlight);
		cnv.dragLeave(unhighlight);
		// file drag and drop
		cnv.drop((file) => {
			let pairs = document.createElement('div')
			let img = document.createElement('img')
			let edges = document.createElement('img')
			pairs.appendChild(edges)
			pairs.appendChild(img)
			extraImagesDiv.appendChild(pairs)

			p.loadImage(file.data, (i) => { edges.src = file.data
				gfx.background(255)
				gfx.image(i, 0, 0, cwidth, cheight)
				convert(file.data, [img, resultImg])});

		},() => {
			unhighlight()
			// erase previous images
			extraImagesDiv.innerHTML = ''
		})

        eraserToggle.onchange = (e) => {
            if (e.target.checked) {
                currentWeight = eraserWeight
                gfx.stroke(255)
				isErasing = true
            } else {
                currentWeight = defaultBrushWeight
                gfx.stroke(0)
				isErasing = false
            }

            gfx.strokeWeight(currentWeight)
        }

        btn.onclick = () => {
			smallgfx.image(gfx,0,0,128,128)
            smallgfx.filter(p.THRESHOLD, 0.99)
            let dataUrl = smallgfx.canvas.toDataURL()

			convert(dataUrl, [resultImg])
        }

        eraserSlider.onchange = (e) => {
          // if erasing, update gfx.strokeWeight
		  if (isErasing) {
		  eraserWeight = p.map(e.target.value, 0, 1, p.width / 128 * 10, p.width / 128 * 50)
			  currentWeight = eraserWeight
		  }
        }

        clearButton.onclick = () => {
			gfx.background(255)
			extraImagesDiv.innerHTML = ''
			resultImg.src = ''
		}

        gfx.ellipseMode(p.CENTER)
        gfx.fill(0)
        gfx.strokeWeight(defaultBrushWeight)

        gfx.background(255)
    }

    p.draw = () => {
        p.image(gfx,0,0)

		p.noFill()
		p.strokeWeight(1)
		p.ellipse(p.mouseX, p.mouseY, currentWeight, currentWeight)
    }

    p.mouseDragged = () => {
		gfx.strokeWeight(currentWeight)
        gfx.line(p.pmouseX, p.pmouseY, p.mouseX, p.mouseY)
    }

    p.mouseMoved = () => {
        // p.ellipse(p.mouseX, p.mouseY, currentWeight, currentWeight)
    }

	function highlight() {
		  cnv.style('border','5px dashed #F00');
	}

	function unhighlight() {
		  cnv.style('border','1px solid #000');
	}

	function convert(dataUrl, imageElts) {
		// send data to backend via js fetch API
		const data = { imageData: dataUrl };

		fetch('/convert', {
			method: 'POST',
			headers: {
				'Content-Type': 'application/json',
			},
			body: JSON.stringify(data),
		})
		.then((response) => response.json())
		.then((data) => {
			let convertedImageData = data.imageData
			// process data sent back from server
			for(let i=0; i<imageElts.length; i++) {
				imageElts[i].src = convertedImageData
			}
		})
		.catch((error) => {
			console.error('Error:', error);
		});
		
		// DEBUG
		resultImg.src = dataUrl
	}
}

let myp5 = new p5(mysketch)
