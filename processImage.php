<?php

$upload_dir = 'uploads/';
if (!file_exists($upload_dir)) {
    mkdir($upload_dir, 0777, true);
}

// Check if a file has been uploaded
if (isset($_FILES['image']) && $_FILES['image']['error'] === UPLOAD_ERR_OK) {
    // Get the uploaded file's details
    $image_file = $_FILES['image'];
    $file_name = $image_file['name'];
    $file_tmp_name = $image_file['tmp_name'];

    // Save the uploaded image to the server
    $target_file = $upload_dir . basename($file_name);
    if (move_uploaded_file($file_tmp_name, $target_file)) {
        echo "Image uploaded successfully. Processing...<br>";
    } else {
        echo "Sorry, there was an error uploading your file.";
    }
} else {
    echo "No file uploaded or there was an upload error.";
}

$python_script_path = 'pic_to_shapes.py';
$python_command = "python3 pic_to_shapes.py" . escapeshellarg($uploaded_file_path)";

// Execute the Python script and capture output
exec($python_command, $output, $status);

if ($status === 0) {
    echo "Python script ran successfully!<br>";
    return $output
}
else {
    echo "Error running Python script.<br>";
}

?>