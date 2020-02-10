# a python script to help some mouse intensive clicking tasks
# default keys are
# use F1/F2 to make mouse1 hold down/up
# use F3/F4 to make mouse2 hold down/up
# use F5/F6 to make mouse1 click rapidly
# use F7/F8 to make mouse2 click rapidly
# use F9 to stop script

import pyautogui
import time
import keyboard

m1down = 'F1'
m1up = 'F2'
m2down = 'F3'
m2up = 'F4'
m1rclick = 'F5'
m1rclickstop = 'F6'
m2rclick = 'F7'
m2rclickstop = 'F8'
quitb = 'F9'

alternate_mouse1 = False
alternate_mouse2 = False
m1_up = True
m2_up = True

on = True
while on:
  # change left mouse button up/down
  if keyboard.is_pressed(m1down):
    pyautogui.mouseUp()
    pyautogui.mouseDown()
  if keyboard.is_pressed(m1up):
    pyautogui.mouseUp()

  # change right mouse button up/down
  if keyboard.is_pressed(m2down):
    pyautogui.mouseUp(button='right')
    pyautogui.mouseDown(button='right')
  if keyboard.is_pressed(m2up):
    pyautogui.mouseUp(button='right')

  # change if mouse2 is alternating
  if keyboard.is_pressed(m1rclick):
    alternate_mouse1 = True
  
  if keyboard.is_pressed(m1rclickstop):
    alternate_mouse1 = False

  # perform quick "clicks" on mouse2 button
  if alternate_mouse1:
    if m1_up:
      pyautogui.mouseDown()
      m1_up = False
    else:
      pyautogui.mouseUp()
      m1_up = True

  # change if mouse2 is alternating
  if keyboard.is_pressed(m2rclick): 
    alternate_mouse2 = True
  
  if keyboard.is_pressed(m2rclickstop):
    alternate_mouse2 = False

  # perform quick "clicks" on mouse2 button
  if alternate_mouse2:
    if m2_up:
      pyautogui.mouseDown(button='right')
      m2_up = False
    else:
      pyautogui.mouseUp(button='right')
      m2_up = True
  
  # quit program
  if keyboard.is_pressed(quitb):
    on = False