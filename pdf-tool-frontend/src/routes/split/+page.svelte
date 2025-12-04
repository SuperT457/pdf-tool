<script>
    let file = null;

    function handleFile(e) {
        console.log(e)
        file = e.target.files[0];
    }

    function upload(){
        if (!file){
            return alert("Provide a file!")
        }
        alert("File uploaded correctly")
    }

</script>

<h1>Split your PDF document</h1>
<p>Upload your document and cut only the pages you need</p>

<input type="file" accept="application/pdf" on:change={handleFile} />
<button on:click={upload}>Upload</button>