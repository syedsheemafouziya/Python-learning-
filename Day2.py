{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNrKWqX6MhNbIbWEvwpUvxE",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/syedsheemafouziya/Python-learning-/blob/main/Day2.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "5e0f1ljdFDzq",
        "outputId": "f3eaefed-3335-49b5-d6f3-9539ac2fa875"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "write a sentence: Syed sheema fouziya \n",
            "total words: 3\n",
            "total vowels: 8\n"
          ]
        }
      ],
      "source": [
        "sentence=input(\"write a sentence: \")\n",
        "words=sentence.split()\n",
        "print(\"total words:\",len(words))\n",
        "\n",
        "count=0\n",
        "vowels=\"aeiouAEIOU\"\n",
        "for ch in sentence:\n",
        "    if ch in vowels:\n",
        "        count+=1\n",
        "print(\"total vowels:\",count)"
      ]
    }
  ]
}