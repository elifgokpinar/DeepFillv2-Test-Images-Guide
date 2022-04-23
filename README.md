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
  <li>Generate masked images <a href="https://github.com/elifgokpinar/DeepFillv2-Test-Images-Guide/tree/main/Generate%20Masked%20Images">(link)</a>. I used <a href=https://www.dropbox.com/s/01dfayns9s0kevy/test_mask.zip?dl=0>NVIDIA Irregular Mask Dataset: Testing Set</a>.
</li>
  <li>Generate test commands file  <a href="https://github.com/elifgokpinar/DeepFillv2-Test-Images-Guide/tree/main/Generate%20Test%20Commands">(link)</a>. (The system takes 2 inputs to test : masked image and mask image. Pay attention the masked image and mask image paths while generating test command file.)</li>
  <li>Run the commands file in your computer</li>
</ul>

<h2>Examples</h2>

![masked_image_9](https://user-images.githubusercontent.com/72789565/164889078-d2cd42cc-7d0f-4242-bf0d-7945684ba018.png) ![9](https://user-images.githubusercontent.com/72789565/164889111-12275eb9-dbc3-47ce-8f40-a5f595428a63.png) ![00008](https://user-images.githubusercontent.com/72789565/164889148-56e87c38-7624-4465-ba5a-d50481601d6c.png)


![masked_image_6](https://user-images.githubusercontent.com/72789565/164889315-9eb7f384-980f-47a6-9152-c95775c5b970.png)
 ![6](https://user-images.githubusercontent.com/72789565/164889285-de209c5b-1f08-410b-bdde-8a3577a7ef58.png)
 ![00005](https://user-images.githubusercontent.com/72789565/164889274-fa781ab0-a7a0-4363-b073-949f03686c05.png)

From celeba_hq dataset. First column shows masked image, second column shows mask image and third column shows inpainting result.

## Citing
```
@article{yu2018generative,
  title={Generative Image Inpainting with Contextual Attention},
  author={Yu, Jiahui and Lin, Zhe and Yang, Jimei and Shen, Xiaohui and Lu, Xin and Huang, Thomas S},
  journal={arXiv preprint arXiv:1801.07892},
  year={2018}
}

@article{yu2018free,
  title={Free-Form Image Inpainting with Gated Convolution},
  author={Yu, Jiahui and Lin, Zhe and Yang, Jimei and Shen, Xiaohui and Lu, Xin and Huang, Thomas S},
  journal={arXiv preprint arXiv:1806.03589},
  year={2018}
}
```


