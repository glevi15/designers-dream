let mysketch = (p) => {
    let cwidth = 500
    let cheight = 500
    let defaultBrushWeight = cwidth / 125
    let eraserWeight = defaultBrushWeight * 10
    let currentWeight = defaultBrushWeight

    let smallgfx;
    let gfx;

    p.setup = () => {
        cnv = p.createCanvas(cwidth, cheight)
        cnv.parent('canvasContainer')
        
        gfx = p.createGraphics(cwidth, cheight)
        smallgfx = p.createGraphics(125,125)
        
        let eraserToggle = document.getElementById("eraserToggle")
        let btn = document.getElementById("convertButton")
        let eraserSlider = document.getElementById("eraserSizeSlider")

        eraserToggle.onchange = (e) => {
            if (e.target.checked) {
                currentWeight = eraserWeight
                gfx.stroke(255)
            } else {
                currentWeight = defaultBrushWeight
                gfx.stroke(0)
            }

            gfx.strokeWeight(currentWeight)
        }

        btn.onclick = () => {
            let resultImg = document.getElementById("resultImg")

            smallgfx.image(gfx,0,0,125,125)
            smallgfx.filter(p.THRESHOLD, 0.9)
            let dataUrl = smallgfx.canvas.toDataURL()

            // send data to backend via js fetch API
            fetch("/convert", {
                method: 'POST',
                body: {
                    imageData: dataUrl
                },
            }).then(response => {
                console.log(response)
            }).then(data => {
                // process data sent back from server
                // get data.convertedDataUrl or convertedImageData or whatever
            })

            // resultImg.src = convertedImageData
            // for now just display what we sent to server as it is
            resultImg.src = dataUrl
        }

        eraserSlider.onchange = (e) => {
            eraserWeight = p.map(e.target.value, 0, 1, p.width / 125 * 10, p.width / 125 * 50)
        }

        gfx.ellipseMode(p.CENTER)
        gfx.fill(0)
        gfx.strokeWeight(defaultBrushWeight)

        gfx.background(255)
    }

    p.draw = () => {
        p.image(gfx,0,0)
    }

    p.mouseDragged = () => {
        gfx.line(p.pmouseX, p.pmouseY, p.mouseX, p.mouseY)
    }

    p.mouseMoved = () => {
        // p.ellipse(p.mouseX, p.mouseY, currentWeight, currentWeight)
    }
}

let myp5 = new p5(mysketch)