# DeepFillv2 Test Images Guide
Test stages of Gated Convolution (DeepFillv2) inpainting method are explained.

<h2>Requirements</h2>
<ul>
  <li>Install python3.</li>
  <li>Install tensorflow (tested on Release 1.3.0, 1.4.0, 1.5.0, 1.6.0, 1.7.0).</li>
</ul>

<h4>I used Python 3.7, Tensorflow 1.15, CUDA 10</h4>

<h2>Test Stages</h2>
<ul>
  <li>Install software requirements</li>
  <li>Clone the deepfillv2 github project on your computer = <code>git clone https://github.com/JiahuiYu/generative_inpainting</code></li>
  <li>Install tensorflow toolkit neuralgym (run <code>pip install git+https://github.com/JiahuiYu/neuralgym</code>)</li>
  <li>Generate masked images <a href="https://github.com/elifgokpinar/DeepFillv2-Test-Images-Guide/tree/main/Generate%20Masked%20Images">link</a></li>
  <li>Generate test commands file  <a href="https://github.com/elifgokpinar/DeepFillv2-Test-Images-Guide/tree/main/Generate%20Test%20Commands">link</a> (The system takes 2 inputs to test : masked image and mask image. Pay attention the masked image and mask image paths while generating test command file.)</li>
  <li>Run the commands file in your computer</li>
</ul>


