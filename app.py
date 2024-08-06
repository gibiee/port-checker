import gradio as gr
import socket

resp_message = {0: 'Opened',
                10061: 'Opened but nothing',
                10060: 'Closed'}

def check(ip: str, port: int, timeout: int) :
    print(ip, port, timeout)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s :
        s.settimeout(timeout)
        resp = s.connect_ex((ip, port))

    if resp_message.get(resp, False) :
        return [resp, resp_message[resp]]
    else :
        return [resp, "Unknown"]

with gr.Blocks() as demo :
    gr.Markdown("""
                # Port Checker
                ### Output will be returned one of the 4 states.
                ① Opened (0)  
                ② Opened but nothing (10061)  
                ③ Closed (10060)  
                ④ Unknown (others)  
                """)
    
    with gr.Row() :
        with gr.Column() :
            input_ip = gr.Textbox(label='ip', value="127.0.0.1")
            input_port = gr.Number(label='port', value=80, precision=0)
            input_timeout = gr.Number(label='timeout', value=10, precision=0)
            btn = gr.Button(value="Check", variant='primary')
        
        with gr.Column() :
            output_errno = gr.Textbox(label='errno', interactive=False)
            output_state = gr.Textbox(label='state', interactive=False)

    btn.click(fn=check, inputs=[input_ip, input_port, input_timeout], outputs=[output_errno, output_state])

demo.launch()