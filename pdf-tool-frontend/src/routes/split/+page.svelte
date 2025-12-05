<script>
    let file = null;

    function handleFile(e) {
        console.log(e)
        file = e.target.files[0];
    }

    async function split(){
        if (!file){
            return alert("Provide a file!");
        }
        
        const formData = new FormData();
        formData.append("file",file);

        const res = await fetch("http://localhost:8000/api/split",{method:"POST",body:formData});
        
        if (!res.ok){
            return alert("Error while processing PDF");
        }

        const blob = await res.blob();

        const url = URL.createObjectURL(blob);

        const link = document.createElement("a");
        link.href = url;
        // link.download = "download.pdf";
        link.click();

        URL.revokeObjectURL(url);
    }

</script>

<h1>Split your PDF document</h1>
<p>Upload your document and cut only the pages you need</p>

<input type="file" accept="application/pdf" on:change={handleFile} />
<button on:click={split}>Upload</button>