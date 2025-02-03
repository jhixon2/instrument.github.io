<?php

// Directory to save uploaded files
$upload_dir = 'uploads/';
if (!file_exists($upload_dir)) {
    mkdir($upload_dir, 0777, true);
}

// Check if a file has been uploaded
if (isset($_FILES['video']) && $_FILES['video']['error'] === UPLOAD_ERR_OK) {
    // Get the uploaded file's details
    $video_file = $_FILES['video'];
    $file_name = $video_file['name'];
    $file_tmp_name = $video_file['tmp_name'];

    // Save the uploaded video to the server
    $target_file = $upload_dir . basename($file_name);
    if (move_uploaded_file($file_tmp_name, $target_file)) {
        echo "Video uploaded successfully. Processing...<br>";

        processVideo($target_file);
    } else {
        echo "Sorry, there was an error uploading your file.";
    }
} else {
    echo "No file uploaded or there was an upload error.";
}

function processVideo($video_path) {
    $output_dir = 'frames/';
    if (!file_exists($output_dir)) {
        mkdir($output_dir, 0777, true);
    }

    // Command to extract frames and resize them
    $cmd = "ffmpeg -i " . escapeshellarg($video_path) . " -vf scale=64:-1 " . escapeshellarg($output_dir . "frame_%03d.png");

    exec($cmd, $output, $status);
    
    if ($status === 0) {
        echo "Frames extracted and resized successfully.<br>";

        $frame_files = glob($output_dir . "*.png");
        foreach ($frame_files as $frame_file) {
            analyzeFrame($frame_file);
        }
    } else {
        echo "Error processing video with FFmpeg.";
    }
}

function analyzeFrame($frame_path) {
    $image = imagecreatefrompng($frame_path);
    $width = imagesx($image);
    $height = imagesy($image);

    // Iterate through all pixels
    for ($y = 0; $y < $height; $y++) {
        for ($x = 0; $x < $width; $x++) {
            $rgb = imagecolorat($image, $x, $y);
            $r = ($rgb >> 16) & 0xFF;
            $g = ($rgb >> 8) & 0xFF;
            $b = $rgb & 0xFF;
            echo "Pixel ($x, $y): R=$r, G=$g, B=$b<br>";
        }
    }

    imagedestroy($image);

}
?>